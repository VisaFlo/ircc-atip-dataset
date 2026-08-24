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


def test_ocr_dropped_i_in_ircc_still_deflects():
    # Real thread (A-2025-81965_00760.md, "Co-op work authorization while
    # application in process"): pure refusal, but OCR printed "RCC Web form"
    # (dropped I) and left "Categories: Case Specific Request" residue plus
    # the torn "no further action will be taken..." tail. All three must
    # strip, or this boilerplate-only reply misfiles as answered.
    answer = (
        "Dec-25\nCategories: Case Specific Request\nHello,\n"
        "Thank you for contacting the Immigration Representatives Mailbox.\n"
        "Please note that we do not answer case specific inquiries, and no "
        "further action will be taken including forwarding emails to any "
        "team/department or any further correspondence. The Immigration "
        "Representative inbox is responsible for general enquiries received "
        "from authorized immigration representatives and lawyers with respect "
        "to general procedures and operational policies for the various "
        "immigration lines of business including permanent residence, "
        "temporary residence, asylum, citizenship and program integrity.\n"
        "For updates on applications outside of normal processing times, "
        "requests for expedited processing of an application, or if clients "
        "wish to report important changes to their application information, "
        "please fill out the RCC Web form-Canada.ca or you can use existing "
        "client support channels available on our website to communicate "
        "with us.\nThank you,\nThe Immigration Representatives Mailbox"
    )
    t = {"subject": "Co-op work authorization while application in process",
         "date": "2025-11-14", "raw": answer, "question": None, "answer": answer}
    assert classify(t) == "deflected"


def test_line_wrapped_deflection_signal_is_found():
    # Real thread (A-2025-85182_00520.md, "Clarification on PGWP Eligibility -
    # Involuntary Part-Time Semester"): OCR wraps "case-\nspecific" across a
    # line break, so signals must be searched on whitespace-collapsed text.
    # The body beyond boilerplate is only a webpage pointer -> deflected.
    answer = (
        "Good day,\nThank you for contacting the Immigration Representatives "
        "Mailbox. Please note that this mailbox is intended for general "
        "guidance and does not provide responses to case-\nspecific inquiries "
        "but have provided the following information as guidance. If you have "
        "case specific\nquestions about a file, you are encouraged to submit "
        "the IRCC Web form.\nPlease see our response to your question.\n"
        "*** Please review Part-time status for final academic session' in "
        "Post-graduation work permit (PGWP) [R205(c) - C43] -\nInternational "
        "Mobility Program-Canada.ca. We hope you find this information "
        "helpful.\nThank you kindly,\nThe Immigration Representatives Mailbox"
    )
    t = {"subject": "Clarification on PGWP Eligibility", "date": "2025-11-27",
         "raw": answer, "question": None, "answer": answer}
    assert classify(t) == "deflected"


def test_stamp_pattern_spares_year_ranges():
    # "2024-2026" looks like a tracking stamp to a naive 20\d{2}-\d{3,4}
    # pattern but is a year range; it must survive stripping.
    from pipeline.quality import strip_boilerplate
    kept = strip_boilerplate("Details are in the 2024-2026 Immigration Levels Plan.")
    assert "2024-2026 Immigration Levels Plan" in kept
    # while real stamps still strip:
    assert "REP-B-2025-2095" not in strip_boilerplate("REP-B-2025-2095 - Due 28-Nov-25 some text")
    assert "(AB-2025-269)" not in strip_boilerplate("(AB-2025-269) - Due Nov 29/25 some text")


# ------------------------------------------------------------------ sweep

@pytest.mark.parametrize(
    "fixture",
    ["normal_thread.md", "deflected_thread.md", "inline_qa_chunk.md", "boundary_chunk.md", "oldformat_chunk.md"],
)
def test_classify_returns_valid_label_for_every_fixture_thread(fixture):
    for t in split_threads((FIXTURES / fixture).read_text()):
        assert classify(t) in {"answered", "deflected", "partial"}
