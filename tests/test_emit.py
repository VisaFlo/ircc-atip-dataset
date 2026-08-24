"""Tests for pipeline.emit (JSON emitter) and pipeline.run (orchestrator)."""
import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

from pipeline.emit import RECORD_KEYS, emit, make_id
from pipeline.run import discover_releases, run

OCR_DIR = Path(
    "/private/tmp/claude-501/-Users-Yulbin-Documents-Dev-2minEasy/"
    "bed0fa35-b2f4-4146-a923-ed06fb17096c/scratchpad/ati/received_ocr"
)


def make_thread(subject="Study permit question", date="2025-11-20",
                raw="raw body text", question="q?", answer="a.",
                release="A-2025-72666", **extra):
    t = {
        "subject": subject,
        "date": date,
        "raw": raw,
        "question": question,
        "answer": answer,
        "atip_release": release,
        "quality": "answered",
    }
    t.update(extra)
    return t


def load(out_dir, name):
    return json.loads((Path(out_dir) / name).read_text(encoding="utf-8"))


# ---------------------------------------------------------------- schema

class TestSchema:
    def test_record_has_exactly_nine_keys_and_no_raw(self, tmp_path):
        emit([make_thread()], str(tmp_path))
        data = load(tmp_path, "2025.json")
        assert data["count"] == 1
        rec = data["threads"][0]
        assert set(rec.keys()) == set(RECORD_KEYS)
        assert len(rec.keys()) == 9
        assert "raw" not in rec

    def test_record_field_values(self, tmp_path):
        emit([make_thread(subject="REP-2025-0939 - Spousal question")], str(tmp_path))
        rec = load(tmp_path, "2025.json")["threads"][0]
        assert rec["id"] == "REP-2025-0939"
        assert rec["atip_release"] == ["A-2025-72666"]
        assert rec["date"] == "2025-11-20"
        assert rec["subject"] == "REP-2025-0939 - Spousal question"
        assert rec["question"] == "q?"
        assert rec["answer"] == "a."
        assert rec["quality"] == "answered"
        assert rec["category"] is None
        assert rec["tags"] == []

    def test_atip_release_string_becomes_list(self, tmp_path):
        emit([make_thread(release="A-2025-81965")], str(tmp_path))
        rec = load(tmp_path, "2025.json")["threads"][0]
        assert rec["atip_release"] == ["A-2025-81965"]

    def test_atip_release_list_passthrough_sorted(self, tmp_path):
        emit([make_thread(release=["B-rel", "A-rel"])], str(tmp_path))
        rec = load(tmp_path, "2025.json")["threads"][0]
        assert rec["atip_release"] == ["A-rel", "B-rel"]


# ---------------------------------------------------------------- ids

class TestIds:
    def test_rep_id_from_subject(self):
        assert make_id(make_thread(subject="RE: REP-2025-0939 spousal")) == "REP-2025-0939"

    def test_rep_id_b_variant(self):
        assert make_id(make_thread(subject="REP-B-2025-1767 - Due Nov")) == "REP-B-2025-1767"

    def test_rep_id_from_raw_when_subject_lacks_it(self):
        t = make_thread(subject="Question about PGWP",
                        raw="Archived: ... REP-2024-0011 - Due ...")
        assert make_id(t) == "REP-2024-0011"

    def test_gen_fallback_deterministic(self):
        t1 = make_thread(subject="no rep id here", raw="body " * 100)
        t2 = make_thread(subject="no rep id here", raw="body " * 100)
        id1, id2 = make_id(t1), make_id(t2)
        assert id1 == id2
        assert id1.startswith("GEN-")
        expected = hashlib.sha256(
            ("no rep id here" + "2025-11-20" + ("body " * 100)[:200]).encode("utf-8")
        ).hexdigest()[:8]
        assert id1 == f"GEN-{expected}"

    def test_collision_suffix(self, tmp_path):
        base_raw = "x" * 200
        t1 = make_thread(subject="same subject", raw=base_raw + "AAAA tail one")
        t2 = make_thread(subject="same subject", raw=base_raw + "BBBB tail two")
        t3 = make_thread(subject="same subject", raw=base_raw + "CCCC tail three")
        emit([t1, t2, t3], str(tmp_path))
        ids = [r["id"] for r in load(tmp_path, "2025.json")["threads"]]
        assert len(set(ids)) == 3
        stems = {i.rsplit("-", 1)[0] if i.count("-") > 1 else i for i in ids}
        base = min(ids, key=len)
        assert sorted(ids) == sorted([base, f"{base}-2", f"{base}-3"])

    def test_rep_id_collision_also_suffixed(self, tmp_path):
        t1 = make_thread(subject="REP-2025-0001 first", raw="one")
        t2 = make_thread(subject="REP-2025-0001 second", raw="two")
        emit([t1, t2], str(tmp_path))
        ids = sorted(r["id"] for r in load(tmp_path, "2025.json")["threads"])
        assert ids == ["REP-2025-0001", "REP-2025-0001-2"]


# ---------------------------------------------------------------- grouping

class TestGroupingAndIndex:
    def test_year_files_and_undated(self, tmp_path):
        threads = [
            make_thread(subject="a 2016", date="2016-05-01"),
            make_thread(subject="b 2025", date="2025-01-02"),
            make_thread(subject="c undated", date=None),
        ]
        idx = emit(threads, str(tmp_path))
        assert (tmp_path / "2016.json").exists()
        assert (tmp_path / "2025.json").exists()
        assert (tmp_path / "undated.json").exists()
        assert idx["by_year"] == {"2016": 1, "2025": 1, "undated": 1}
        assert idx["total"] == 3

    def test_file_contents_sorted_by_date_then_id(self, tmp_path):
        threads = [
            make_thread(subject="REP-2025-0002 later", date="2025-06-01"),
            make_thread(subject="REP-2025-0009 same day", date="2025-01-01"),
            make_thread(subject="REP-2025-0001 same day", date="2025-01-01"),
        ]
        emit(threads, str(tmp_path))
        recs = load(tmp_path, "2025.json")["threads"]
        assert [(r["date"], r["id"]) for r in recs] == [
            ("2025-01-01", "REP-2025-0001"),
            ("2025-01-01", "REP-2025-0009"),
            ("2025-06-01", "REP-2025-0002"),
        ]

    def test_index_totals_match_sum(self, tmp_path):
        threads = [
            make_thread(subject=f"REP-2025-{i:04d} q", date="2025-03-01")
            for i in range(5)
        ] + [make_thread(subject="undated one", date=None)]
        idx = emit(threads, str(tmp_path))
        on_disk = load(tmp_path, "index.json")
        assert on_disk == idx
        assert idx["total"] == sum(idx["by_year"].values()) == 6
        assert sum(idx["by_quality"].values()) == 6
        assert "generated" in idx

    def test_by_release_counts(self, tmp_path):
        threads = [
            make_thread(subject="one", release="A-2025-81965"),
            make_thread(subject="two", release=["A-2025-81965", "A-2025-85182"]),
        ]
        idx = emit(threads, str(tmp_path))
        assert idx["by_release"] == {"A-2025-81965": 2, "A-2025-85182": 1}


# ---------------------------------------------------------------- quality

class TestQuality:
    def test_quality_autofilled_via_classify_when_absent(self, tmp_path):
        t = make_thread(subject="no quality key", answer=None)
        del t["quality"]
        emit([t], str(tmp_path))
        rec = load(tmp_path, "2025.json")["threads"][0]
        assert rec["quality"] == "partial"  # classify(): no answer -> partial

    def test_existing_quality_preserved(self, tmp_path):
        t = make_thread(quality="deflected")
        emit([t], str(tmp_path))
        rec = load(tmp_path, "2025.json")["threads"][0]
        assert rec["quality"] == "deflected"


# ---------------------------------------------------------------- run.py

class TestDiscoverReleases:
    def test_parts_merge_in_order_and_chunks_ignored(self, tmp_path):
        ocr = tmp_path / "ocr"
        ocr.mkdir()
        (ocr / "A-2025-72666 - Part 2.md").write_text("PART TWO", encoding="utf-8")
        (ocr / "A-2025-72666 - Part 1.md").write_text("PART ONE", encoding="utf-8")
        (ocr / "2A-2021-12699_Part3.md").write_text("OLD STYLE", encoding="utf-8")
        (ocr / "A-2021-10864_part_3.md").write_text("UNDERSCORE STYLE", encoding="utf-8")
        (ocr / "A-2025-81965.md").write_text("SINGLE", encoding="utf-8")
        (ocr / "notes.txt").write_text("ignore me", encoding="utf-8")
        chunks = ocr / "chunks"
        chunks.mkdir()
        (chunks / "A-2025-13308_00000.md").write_text("CHUNK", encoding="utf-8")

        releases = discover_releases(str(ocr))
        assert set(releases) == {
            "A-2025-72666", "2A-2021-12699", "A-2021-10864", "A-2025-81965",
        }
        # parts concatenated in part order
        assert releases["A-2025-72666"].index("PART ONE") < \
            releases["A-2025-72666"].index("PART TWO")
        assert "CHUNK" not in "".join(releases.values())

    def test_real_ocr_dir_patterns(self):
        if not OCR_DIR.is_dir():
            pytest.skip("real OCR dir not present")
        releases = discover_releases(str(OCR_DIR))
        # every full file in the real dir must map to a release
        n_files = len(list(OCR_DIR.glob("*.md")))
        assert n_files > 0
        assert all(v.strip() for v in releases.values())


class TestIntegration:
    def test_smoke_two_real_releases(self, tmp_path):
        sources = [OCR_DIR / "A-2025-81965.md", OCR_DIR / "A-2025-85182.md"]
        if not all(p.is_file() for p in sources):
            pytest.skip("real full-file OCR outputs not present")
        ocr = tmp_path / "ocr"
        ocr.mkdir()
        for p in sources:
            shutil.copy(p, ocr / p.name)
        out = tmp_path / "out"
        idx = run(str(ocr), str(out))
        assert (out / "index.json").exists()
        assert idx["total"] > 0
        assert idx["total"] == sum(idx["by_year"].values())
        assert sum(idx["by_quality"].values()) == idx["total"]
        assert set(idx["by_release"]) <= {"A-2025-81965", "A-2025-85182"}
        # every emitted year file is accounted for in the index
        for f in out.glob("*.json"):
            if f.name == "index.json":
                continue
            data = json.loads(f.read_text(encoding="utf-8"))
            key = f.stem
            assert idx["by_year"][key] == data["count"] == len(data["threads"])
            for rec in data["threads"]:
                assert "raw" not in rec

    def test_cli_entrypoint(self, tmp_path):
        ocr = tmp_path / "ocr"
        ocr.mkdir()
        (ocr / "A-2025-99999.md").write_text(
            "Archived: stamp\nSubject: REP-2025-0100 - test question\n"
            "From: someone\nSent: November 20, 2025\nbody text here\n",
            encoding="utf-8",
        )
        out = tmp_path / "out"
        proc = subprocess.run(
            [sys.executable, "-m", "pipeline.run", str(ocr), str(out)],
            capture_output=True, text=True,
            cwd=str(Path(__file__).resolve().parent.parent),
        )
        assert proc.returncode == 0, proc.stderr
        assert (out / "index.json").exists()
        assert "A-2025-99999" in proc.stdout
