"""Tests for pipeline.split_threads — thread splitter for OCR'd IRCC mailbox releases."""
from pathlib import Path

import pytest

from pipeline.split_threads import normalize_subject, split_threads

FIXTURES = Path(__file__).parent / "fixtures"


def load(name: str) -> str:
    return (FIXTURES / name).read_text(encoding="utf-8")


class TestBoundaries:
    def test_boundary_chunk_splits_into_multiple_threads(self):
        threads = split_threads(load("boundary_chunk.md"))
        assert len(threads) >= 2

    def test_every_boundary_thread_has_subject(self):
        threads = split_threads(load("boundary_chunk.md"))
        for t in threads:
            assert t["subject"], f"thread with empty subject, raw head: {t['raw'][:120]!r}"

    def test_thread_subjects_are_normalized(self):
        import re

        threads = split_threads(load("boundary_chunk.md"))
        for t in threads:
            assert not re.match(r"(?i)^(re|fw|fwd|tr)\s*:", t["subject"]), t["subject"]

    def test_raw_is_verbatim_slice_of_input(self):
        text = load("boundary_chunk.md")
        threads = split_threads(text)
        for t in threads:
            assert t["raw"] in text


class TestQuestionAnswer:
    def test_normal_thread_has_qa_pair_with_substantive_answer(self):
        threads = split_threads(load("normal_thread.md"))
        qa = [t for t in threads if t["question"] and t["answer"]]
        assert qa, "expected at least one thread with both question and answer"
        # Pin the CUAET study-permit thread: the IRCC reply (answer side) carries
        # the substantive phrase, the external question side identifies an RCIC.
        cuaet = [t for t in qa if t["subject"].startswith("Study Permit application under the CUAET")]
        assert cuaet, "CUAET thread not found among Q&A threads"
        assert "letter of acceptance" in cuaet[0]["answer"].lower()
        assert "Regulated Canadian Immigration Consultant" in cuaet[0]["question"]
        assert "letter of acceptance" not in cuaet[0]["question"].lower()

    def test_answer_bodies_are_stripped_of_noise(self):
        threads = split_threads(load("normal_thread.md"))
        for t in threads:
            for body in (t["question"], t["answer"]):
                if body is None:
                    continue
                assert "CAUTION: This email originated" not in body
                assert "Information disclosed under the Access" not in body
                assert "CHUNK_BOUNDARY" not in body

    def test_dates_are_iso_when_present(self):
        threads = split_threads(load("normal_thread.md"))
        dated = [t for t in threads if t["date"]]
        assert dated, "expected at least one parseable Sent: date"
        for t in dated:
            assert len(t["date"]) == 10 and t["date"][4] == "-" and t["date"][7] == "-"
        # First thread's answer email was sent Friday, November 21, 2025.
        assert threads[0]["date"] == "2025-11-21"


class TestSubjectNormalization:
    def test_strips_repeated_reply_prefixes(self):
        assert normalize_subject("RE: RE: Inquiry: X") == "Inquiry: X"

    def test_strips_forward_prefix_but_keeps_rest(self):
        assert (
            normalize_subject("FW: Question - REP-2018-0618 -")
            == "Question - REP-2018-0618 -"
        )

    def test_mixed_prefixes_and_spacing(self):
        assert normalize_subject("RE : FW: TR: Sujet important") == "Sujet important"

    def test_collapses_whitespace(self):
        assert normalize_subject("  Study   Permit\t question ") == "Study Permit question"


class TestDegenerateInput:
    def test_empty_string(self):
        assert split_threads("") == []

    def test_garbage_without_headers(self):
        assert split_threads("lorem ipsum\nno emails here\n12345\n") == []

    def test_torn_tail_without_subject_is_dropped(self):
        # Text before the first Archived: with no Subject: line is a torn tail.
        assert split_threads("some continuation body text\nwith no headers at all\n") == []
