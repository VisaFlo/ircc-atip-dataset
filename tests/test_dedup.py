"""Tests for pipeline.dedup — cross-release thread deduplication.

The dataset merges ATIP releases whose date ranges overlap (e.g.
1A-2022-39382 covers 2017-01~2022-06 and overlaps A-2021-10864,
A-2021-10866, 2A-2021-90643), so the same email thread can appear in
2+ releases. dedup() collapses those into one thread.
"""
import time
from pathlib import Path

import pytest

from pipeline.dedup import dedup

CHUNKS_DIR = Path(
    "/private/tmp/claude-501/-Users-Yulbin-Documents-Dev-2minEasy/"
    "bed0fa35-b2f4-4146-a923-ed06fb17096c/scratchpad/ati/received_ocr/chunks"
)


def make_thread(subject, date, raw, release, question="q", answer="a"):
    return {
        "subject": subject,
        "date": date,
        "raw": raw,
        "question": question,
        "answer": answer,
        "atip_release": release,
    }


class TestMerging:
    def test_exact_duplicate_pair_merges(self):
        a = make_thread("Study permit for spouse", "2020-03-10", "short raw", "A-2021-10864")
        b = make_thread("Study permit for spouse", "2020-03-11",
                        "much longer raw with more complete OCR text", "1A-2022-39382")
        out = dedup([a, b])
        assert len(out) == 1
        t = out[0]
        assert t["atip_release"] == ["1A-2022-39382", "A-2021-10864"]
        assert t["raw"] == b["raw"]

    def test_similar_but_distinct_subjects_not_merged(self):
        a = make_thread("Study permit for spouse", "2020-03-10", "raw a", "A-2021-10864")
        b = make_thread("Work permit for spouse", "2020-03-10", "raw b", "1A-2022-39382")
        out = dedup([a, b])
        assert len(out) == 2

    def test_same_subject_dates_10_days_apart_not_merged(self):
        a = make_thread("PGWP eligibility question", "2020-03-01", "raw a", "A-2021-10864")
        b = make_thread("PGWP eligibility question", "2020-03-11", "raw b", "1A-2022-39382")
        out = dedup([a, b])
        assert len(out) == 2

    def test_both_dates_none_exact_subject_merges(self):
        a = make_thread("Restoration of status", None, "raw a", "A-2021-10864")
        b = make_thread("Restoration of status", None, "raw b longer", "1A-2022-39382")
        out = dedup([a, b])
        assert len(out) == 1
        assert out[0]["atip_release"] == ["1A-2022-39382", "A-2021-10864"]
        assert out[0]["raw"] == b["raw"]

    def test_both_dates_none_different_subject_not_merged(self):
        a = make_thread("Restoration of status", None, "raw a", "A-2021-10864")
        b = make_thread("Restoration of my status", None, "raw b", "1A-2022-39382")
        out = dedup([a, b])
        assert len(out) == 2

    def test_triple_duplicate_across_three_releases(self):
        a = make_thread("Bridging open work permit", "2021-01-05", "raw one", "A-2021-10866")
        b = make_thread("Bridging open work permit", "2021-01-06",
                        "raw two is the longest of all three", "1A-2022-39382")
        c = make_thread("Bridging open work permit", "2021-01-07", "raw three+", "2A-2021-90643")
        out = dedup([a, b, c])
        assert len(out) == 1
        t = out[0]
        assert t["atip_release"] == ["1A-2022-39382", "2A-2021-90643", "A-2021-10866"]
        assert t["raw"] == b["raw"]

    def test_missing_atip_release_tolerated(self):
        a = {"subject": "Visitor record", "date": "2020-06-01", "raw": "raw a",
             "question": "q", "answer": "a"}
        b = make_thread("Visitor record", "2020-06-02", "raw b longer text", "A-2021-10864")
        out = dedup([a, b])
        assert len(out) == 1
        assert out[0]["atip_release"] == ["A-2021-10864"]

    def test_unmerged_thread_release_normalized_to_list(self):
        a = make_thread("Unique subject one", "2020-01-01", "raw", "A-2021-10864")
        out = dedup([a])
        assert len(out) == 1
        assert out[0]["atip_release"] == ["A-2021-10864"]

    def test_input_not_mutated(self):
        a = make_thread("Study permit", "2020-03-10", "raw a", "A-2021-10864")
        b = make_thread("Study permit", "2020-03-11", "raw b longer", "1A-2022-39382")
        dedup([a, b])
        assert a["atip_release"] == "A-2021-10864"
        assert b["atip_release"] == "1A-2022-39382"


class TestPerformance:
    def test_5k_synthetic_threads_under_30s(self):
        import random
        rng = random.Random(42)
        subjects = [
            "Study permit application processing time",
            "Work permit for spouse of student",
            "PGWP eligibility after online studies",
            "Express Entry proof of funds question",
            "Visitor visa extension inside Canada",
            "Restoration of temporary resident status",
            "Bridging open work permit while PR pending",
            "Biometrics exemption for repeat applicants",
        ]
        threads = []
        for i in range(5000):
            base = rng.choice(subjects)
            # ~half are near-duplicates of a base subject, rest unique-ified
            if i % 2 == 0:
                subj = base
            else:
                subj = f"{base} case {i}"
            month = rng.randint(1, 12)
            day = rng.randint(1, 28)
            date = f"20{rng.randint(17, 22):02d}-{month:02d}-{day:02d}"
            threads.append(make_thread(subj, date, f"raw body {i} " * rng.randint(1, 20),
                                       rng.choice(["A-2021-10864", "1A-2022-39382",
                                                   "2A-2021-90643"])))
        start = time.monotonic()
        out = dedup(threads)
        elapsed = time.monotonic() - start
        assert elapsed < 30, f"dedup took {elapsed:.1f}s on 5k threads"
        assert 0 < len(out) <= 5000


class TestRealData:
    @pytest.mark.skipif(not CHUNKS_DIR.is_dir(), reason="real chunk dir not present")
    def test_real_chunks_two_releases_smoke(self, capsys):
        from pipeline.split_threads import split_threads

        prefixes = ["A-2021-10864", "A-2025-13309"]
        threads = []
        for prefix in prefixes:
            for f in sorted(CHUNKS_DIR.glob(f"{prefix}*.md")):
                for t in split_threads(f.read_text(encoding="utf-8")):
                    t["atip_release"] = prefix
                    threads.append(t)
        assert threads, "no threads parsed from real chunks"
        out = dedup(threads)
        merged = len(threads) - len(out)
        cross = sum(1 for t in out if len(t["atip_release"]) > 1)
        with capsys.disabled():
            print(f"\n[real-data smoke] input={len(threads)} output={len(out)} "
                  f"merged_away={merged} multi_release_threads={cross}")
        assert len(out) <= len(threads)


class TestTrackingStamps:
    """Registrar tracking stamps ("- REP-B-2025-1767 - Due 21-Oct-25") are
    appended to subjects in some releases. They must be stripped for the
    similarity comparison — but a DIFFERENT REP id on each side is positive
    evidence of distinct threads and must block the merge."""

    def test_stamp_suffix_pair_merges(self):
        a = make_thread("2 Questions about IRCC Forms", "2025-10-14", "raw short",
                        "A-2025-81965")
        b = make_thread("2 Questions about IRCC Forms - REP-B-2025-1767 - Due 21-Oct-25",
                        "2025-10-15", "raw longer with the full OCR body", "A-2025-85182")
        out = dedup([a, b])
        assert len(out) == 1
        assert out[0]["atip_release"] == ["A-2025-81965", "A-2025-85182"]
        assert out[0]["raw"] == b["raw"]

    def test_different_rep_ids_do_not_merge(self):
        # After stamp stripping these subjects become IDENTICAL; the differing
        # REP ids are what keep them apart.
        a = make_thread("2 Questions about IRCC Forms - REP-2017-0601",
                        "2017-06-01", "raw a", "A-2021-10864")
        b = make_thread("2 Questions about IRCC Forms - REP-2017-0463",
                        "2017-06-02", "raw b", "1A-2022-39382")
        out = dedup([a, b])
        assert len(out) == 2

    def test_same_rep_id_merges(self):
        a = make_thread("2 Questions about IRCC Forms - REP-2017-0601",
                        "2017-06-01", "raw a", "A-2021-10864")
        b = make_thread("2 Questions about IRCC Forms - REP-2017-0601 - Due 15-Jun-17",
                        "2017-06-02", "raw b is longer than raw a", "1A-2022-39382")
        out = dedup([a, b])
        assert len(out) == 1
        assert out[0]["raw"] == b["raw"]

    def test_unstamped_thread_cannot_bridge_two_rep_ids(self):
        # A stamp-less copy may merge into ONE of the id-bearing threads, but
        # must not transitively fuse two threads with different REP ids.
        a = make_thread("2 Questions about IRCC Forms - REP-2017-0601",
                        "2017-06-01", "raw a", "A-2021-10864")
        b = make_thread("2 Questions about IRCC Forms",
                        "2017-06-02", "raw b no stamp", "1A-2022-39382")
        c = make_thread("2 Questions about IRCC Forms - REP-2017-0463",
                        "2017-06-03", "raw c", "2A-2021-90643")
        out = dedup([a, b, c])
        assert len(out) == 2
