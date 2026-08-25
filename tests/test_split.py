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
        # Exact count for this fixture; regenerating the fixture? update this.
        assert len(threads) == 19

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
        # Joined raws reconstruct the input minus the dropped subject-less head.
        assert text.endswith("".join(t["raw"] for t in threads))


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


class TestOldFormatFallback:
    """Releases without Archived: markers (e.g. A-2021-10864) use Outlook
    header-table exports: From/Sent/To/Cc/Subject cluster with IRCC as sender."""

    def test_oldformat_chunk_splits_into_many_threads(self):
        # Exact count for this fixture (~40 pages, one thread per 2-4 pages);
        # regenerating the fixture? update this.
        threads = split_threads(load("oldformat_chunk.md"))
        assert len(threads) == 17

    def test_oldformat_raw_reconstructs_input(self):
        text = load("oldformat_chunk.md")
        threads = split_threads(text)
        # Joined raws reconstruct the input minus the dropped subject-less head.
        assert text.endswith("".join(t["raw"] for t in threads))

    def test_every_boundary_is_a_from_split_point(self):
        # _OLD_FROM_RE (boundary detection) must never accept a From token that
        # _FROM_RE (email segmentation) rejects: the block would then start
        # with an unrecognized first email, silently swapping question/answer.
        from pipeline.split_threads import _FROM_RE, _oldformat_boundaries

        text = load("oldformat_chunk.md")
        bounds = _oldformat_boundaries(text)
        assert bounds
        for b in bounds:
            # The boundary may start at a "#### " heading prefix before From:.
            assert _FROM_RE.search(text, b, b + 16), f"no From split at {b}"
        # And the tolerance must hold for every OCR variant _OLD_FROM_RE
        # accepts, not just those present in this fixture ("From :" is the
        # variant that diverged once).
        from pipeline.split_threads import _OLD_FROM_RE

        for variant in ["From: X", "From : X", "From  : X", "#### From : X"]:
            assert _OLD_FROM_RE.search(variant)
            assert _FROM_RE.search(variant), f"_FROM_RE rejects {variant!r}"

    def test_oldformat_threads_have_subjects(self):
        threads = split_threads(load("oldformat_chunk.md"))
        for t in threads:
            assert t["subject"], f"empty subject, raw head: {t['raw'][:120]!r}"
        # This thread's header-table Subject: cell is empty (value displaced by
        # OCR); the subject must come from the first NON-empty Subject: line.
        assert "Study Permit Requirement?" in {t["subject"] for t in threads}

    def test_oldformat_has_qa_pairs(self):
        threads = split_threads(load("oldformat_chunk.md"))
        qa = [t for t in threads if t["question"] and t["answer"]]
        assert len(qa) >= len(threads) // 2

    def test_oldformat_answer_is_the_ircc_top_email(self):
        threads = split_threads(load("oldformat_chunk.md"))
        # The DLI-portal thread: IRCC's answer mentions updating the DLI Portal;
        # the question below it asks about study permit notations.
        hits = [
            t for t in threads
            if t["answer"] and "update the DLI Portal" in t["answer"]
        ]
        assert hits, "expected the DLI Portal answer in an answer body"
        assert hits[0]["question"] and "notation" in hits[0]["question"].lower()

    def test_oldformat_some_dates_parse_despite_ocr(self):
        # From/Sent values are often swapped by OCR; the date should still parse
        # for headers with clean month names (e.g. "November 6, 2017").
        threads = split_threads(load("oldformat_chunk.md"))
        assert any(t["date"] and t["date"].startswith("201") for t in threads)
        # This thread's header reads "From: Wednesday, March 1, 2017 12:10 PM
        # Sent:" — the date sits BEFORE the Sent: token and must still parse.
        swapped = [t for t in threads if t["subject"].startswith("Super Urgent")]
        assert swapped and swapped[0]["date"] == "2017-03-01"

    def test_boundary_detector_rejects_quoted_external_header(self):
        from pipeline.split_threads import _oldformat_boundaries

        # Verbatim from A-2025-81965: a QUOTED external question header that has
        # Sent:/Cc:/Subject: but an empty sender zone — not an export boundary.
        external = (
            "esentatives Mailbox\n\n## From:\n\nSent: Friday, August 1, 2025 "
            "12:38 PM Representantsimmigration.IRCC@cic.gc.ca> Cc: Subject: "
            "Closed Work Permits under Start-Up Visa Program\n\nunless you "
            "recognize the sender and know the content is safe.\n"
        )
        assert _oldformat_boundaries(external) == []
        # Verbatim genuine export header (From/Sent values swapped by OCR).
        genuine = (
            "Immigration Representatives / Représentants immigration (IRCC)\n\n"
            "## From:\n\nOctober 1, 2025 4:03 PM\n\n## Sent:\n\nTo: Immigration "
            "Representatives / Représentants immigration (IRCC) Cc: FW: "
            "Clarification-REP-B-2025-1767 - Due 21-Oct-25\n\n# Subject:\n"
        )
        assert len(_oldformat_boundaries(genuine)) == 1


class TestDegenerateInput:
    def test_empty_string(self):
        assert split_threads("") == []

    def test_garbage_without_headers(self):
        assert split_threads("lorem ipsum\nno emails here\n12345\n") == []

    def test_torn_tail_without_subject_is_dropped(self):
        # No Archived: marker and no old-format boundaries either: exercises
        # the no-boundary fallback path, which keeps a lone block only if it
        # carries a Subject: line.
        assert split_threads("some continuation body text\nwith no headers at all\n") == []


class TestInlineQAFallback:
    """A-2025-13309: quoted question emails often lack a From: header — the
    IRCC reply inlines the exchange as Question/Answer(/Response) segments."""

    def test_rfc_style_sent_dates_parse(self):
        threads = split_threads(load("inline_qa_chunk.md"))
        # First thread's header: "Sent: Tue, 1 Oct 2024 14:43:10" (day-first,
        # abbreviated month, no AM/PM).
        assert threads[0]["date"] == "2024-10-01"
        dated = [t for t in threads if t["date"]]
        assert len(dated) >= (len(threads) * 3) // 4

    def test_inline_labels_yield_question_and_answer(self):
        threads = split_threads(load("inline_qa_chunk.md"))
        bowp = [t for t in threads if t["subject"].startswith("Bridging open work permit")]
        assert bowp, "BOWP thread not found"
        t = bowp[0]
        assert t["question"] and "BOWP without AOR" in t["question"]
        assert t["answer"] and "general eligibility requirements" in t["answer"]
        # The labels themselves are stripped from the extracted bodies.
        assert "Question 1" not in t["question"]
        assert "Response 1" not in t["answer"]

    def test_no_labels_means_no_false_extraction(self):
        threads = split_threads(load("inline_qa_chunk.md"))
        t = [
            t for t in threads
            if t["subject"].startswith("Super Visa Application Instructions")
        ][0]
        # Single-From thread without inline markers: best-effort contract
        # unchanged — question stays None, answer keeps the full body.
        assert t["question"] is None
        assert t["answer"]

    def test_threads_with_quoted_question_email_are_untouched(self):
        threads = split_threads(load("inline_qa_chunk.md"))
        t = threads[0]  # DLI off-campus thread: has a real quoted From: email
        assert t["question"] and "off-campus" in t["question"].lower()


class TestRfcHeaderScrub:
    def test_no_rfc_sent_lines_leak_into_bodies(self):
        threads = split_threads(load("inline_qa_chunk.md"))
        for t in threads:
            for body in (t["question"], t["answer"]):
                if body is None:
                    continue
                for line in body.splitlines():
                    assert not line.startswith("Sent:"), f"leaked header: {line!r}"

    def test_mail_received_time_residue_is_scrubbed(self):
        from pipeline.split_threads import _clean_body

        # Verbatim residue shape from A-2021-10864_part_3_00720.
        body = _clean_body(
            "Hello,\n\nMail received time: Mon, 8 May 2017 15:02:30\n\n"
            "Thank you for your enquiry.\n"
        )
        assert "Mail received time" not in body
        assert "Thank you for your enquiry." in body


class TestMixedFormatFiles:
    """Full-file merges can mix formats: A-2021-10864_part_3.md is ~780p of
    old-format exports with a few new-format Archived exports appended at the
    end. Mode selection must be region-aware, not text-global."""

    def test_mixed_tail_splits_both_regions(self):
        # Real slice of the merged file: 3 old-format export clusters followed
        # by 4 Archived exports. Text-global mode selection collapsed the
        # old-format region into a single thread (5 total).
        threads = split_threads(load("mixed_tail.md"))
        assert len(threads) == 7, f"got {len(threads)}"
        for t in threads:
            assert t["subject"], f"empty subject, raw head: {t['raw'][:100]!r}"

    def test_mixed_tail_old_region_threads_are_qa_units(self):
        threads = split_threads(load("mixed_tail.md"))
        # The 3 old-format threads come first (file order), then the archived.
        old, archived = threads[:3], threads[3:]
        assert sum(1 for t in old if t["answer"]) >= 2
        assert all("Archived:" in t["raw"] for t in archived)
        assert not any("Archived:" in t["raw"] for t in old)

    def test_full_merged_file_count_matches_chunk_sweep(self):
        full = Path(
            "/private/tmp/claude-501/-Users-Yulbin-Documents-Dev-2minEasy/"
            "bed0fa35-b2f4-4146-a923-ed06fb17096c/scratchpad/ati/received_ocr/"
            "A-2021-10864_part_3.md"
        )
        if not full.exists():
            pytest.skip("merged source file not on this machine")
        n = len(split_threads(full.read_text()))
        # Chunk-level sweep of the same release yielded 295 threads; the
        # full-file merge must land within +-15% of that.
        assert 251 <= n <= 339, f"full-file count {n} outside 251..339"


def test_ocr_mangled_month_is_recovered():
    """A dotless Turkish "i" in a month name used to raise KeyError and abort a
    whole pipeline run. The look-alike is now normalised, so the date parses."""
    text = (
        "Archived: Monday, aprıl 7, 2025 9:00:00 AM\n"
        "From: Immigration Representatives / Représentants immigration (IRCC)\n"
        "Sent: aprıl 7, 2025 9:00:00 AM\n"
        "Subject: Test thread with mangled month\n"
        "Some answer body text here.\n"
    )
    threads = split_threads(text)
    assert len(threads) == 1
    assert threads[0]["subject"] == "Test thread with mangled month"
    assert threads[0]["date"] == "2025-04-07"


def test_unrecoverable_month_degrades_to_none():
    """A month name we cannot map must yield date=None, never an exception."""
    text = (
        "Archived: Monday, xyzzy 7, 2025 9:00:00 AM\n"
        "From: Immigration Representatives / Représentants immigration (IRCC)\n"
        "Sent: xyzzy 7, 2025 9:00:00 AM\n"
        "Subject: Unmappable month\n"
        "Body text.\n"
    )
    threads = split_threads(text)
    assert len(threads) == 1
    assert threads[0]["date"] is None
