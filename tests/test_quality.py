"""Tests for pipeline.quality.classify — real OCR fixtures, pinned by subject."""
import pathlib

import pytest

from pipeline.quality import classify
from pipeline.split_threads import split_threads

FIXTURES = pathlib.Path(__file__).parent / "fixtures"


def _thread(fixture: str, subject_prefix: str) -> dict:
    threads = split_threads((FIXTURES / fixture).read_text())
    matches = [t for t in threads if t["subject"].startswith(subject_prefix)]
    assert matches, f"no thread with subject prefix {subject_prefix!r} in {fixture}"
    return matches[0]


# --------------------------------------------------------------- deflected

def test_pure_deflection_template_is_deflected():
    # Real answer is ONLY the refusal template: "Please note that we do not
    # answer case specific inquiries. For updates on applications outside of
    # normal processing times, ... please fill out the IRCC Web form-Canada.ca_
    # or you can use existing client support channels ..." — no guidance.
    t = _thread("deflected_thread.md", "Question re LMIA-supported Work Permits for caregivers")
    assert classify(t) == "deflected"


def test_long_channel_list_deflection_is_deflected():
    # 1,233 chars of pure boilerplate: the refusal plus the full support-channel
    # list ("Use the IRCC Web form: ... Telephone: IRCC Client Support Centre
    # 1-888-242-2100 ..."). Long, but zero substance — raw length must not
    # rescue it into "answered".
    t = _thread("deflected_thread.md", "Clarification on C42 Eligibility")
    assert classify(t) == "deflected"


def test_short_refusal_is_deflected():
    # "Thank you for contacting the Immigration Representatives Mailbox.
    # Please note that we do not answer case specific inquiries." and nothing else.
    t = _thread("normal_thread.md", "Inquiry: Clarification on Eligibility for Specialized ECA")
    assert classify(t) == "deflected"


def test_french_out_of_scope_refusal_is_deflected():
    # "Veuillez noter que cette demande ne relève pas de notre compétence et
    # aucune autre mesure ne sera prise ..." + French channel list, no guidance.
    t = _thread("deflected_thread.md", "Nouveau num")
    assert classify(t) == "deflected"


# ---------------------------------------------------------------- answered

def test_substantive_answer_is_answered():
    # Multi-paragraph real guidance on common-law dependent eligibility.
    t = _thread("inline_qa_chunk.md", "Clarification Regarding Common-Law Dependent Eligibility")
    assert classify(t) == "answered"


def test_trap_substantive_answer_with_webform_footer_is_answered():
    # THE TRAP: this answer carries the standard footer "questions about a
    # file, you are encouraged to submit the IRCC Web form." yet also delivers
    # a full substantive answer (the IRPR definition of social assistance and
    # R133(1)(k) sponsorship bar). Footer presence alone must NOT deflect it.
    t = _thread("deflected_thread.md", "Query regarding social assistance")
    assert classify(t) == "answered"
    assert "encouraged to submit the IRCC Web form" in t["answer"]  # trap is real


def test_trap_case_specific_disclaimer_plus_substance_is_answered():
    # Second trap: carries "does not provide responses to case-specific
    # inquiries but have provided the following information as guidance" AND a
    # long substantive answer (medical-exam exemption public policy criteria).
    t = _thread("deflected_thread.md", "Clarification for Exemption to Submit Medicals")
    assert classify(t) == "answered"
    assert "case-specific inquiries" in t["answer"]  # trap is real


# ----------------------------------------------------------------- partial

def test_answer_none_is_partial():
    t = _thread("inline_qa_chunk.md", "Is Canadian self-employed experience considered as foreign")
    assert t["answer"] is None  # pin: this real thread lost its answer to OCR
    assert classify(t) == "partial"


def test_answer_empty_string_is_partial():
    t = {"subject": "x", "date": None, "raw": "Archived: ...", "question": None, "answer": "  "}
    assert classify(t) == "partial"


def test_ocr_error_marker_in_raw_is_partial():
    t = {
        "subject": "x",
        "date": None,
        "raw": "Archived: ... [OCR_ERROR: page unreadable] ...",
        "question": "q",
        "answer": "A long substantive-looking answer " * 20,
    }
    assert classify(t) == "partial"


def test_truncated_fragment_is_partial():
    # Real thread whose answer got torn to a fragment: after the greeting and
    # footer only "before they can continue with the new school or start the
    # new program." survives — a mid-sentence tail, not an answer and not a
    # refusal.
    t = _thread("deflected_thread.md", "Guidance: Study Permit validity after notice of decision")
    assert classify(t) == "partial"


# ------------------------------------------------------------------ sweep

@pytest.mark.parametrize(
    "fixture",
    ["normal_thread.md", "deflected_thread.md", "inline_qa_chunk.md", "boundary_chunk.md", "oldformat_chunk.md"],
)
def test_classify_returns_valid_label_for_every_fixture_thread(fixture):
    for t in split_threads((FIXTURES / fixture).read_text()):
        assert classify(t) in {"answered", "deflected", "partial"}
