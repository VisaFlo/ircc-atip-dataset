"""Split raw OCR markdown of scanned IRCC email release packages into threads.

Each Outlook-archived email export (a block starting at an ``Archived:``
header) is one thread. Within a block, emails are stacked newest-first:
the IRCC answer is on top, the external sender's question below it.
Parsing is best-effort — OCR jumbles header lines and redacts names.
"""
from __future__ import annotations

import re

# ---------------------------------------------------------------- boundaries

# "Archived:" often appears mid-line (glued to a disclosure stamp), so match
# the token anywhere, not only at line start.
_ARCHIVED_RE = re.compile(r"(?=Archived:)")

# Email sub-blocks start at a From header. OCR variants seen in real data:
# "From:", "From :", "From:,", "From Sent:" (colon lost). Must accept at least
# everything _OLD_FROM_RE accepts, or an old-format boundary would start a
# block whose first email is not recognized as a segment (silently swapping
# question and answer).
_FROM_RE = re.compile(r"(?=\bFrom[ \t]*:)|(?=\bFrom,?\s+Sent:)")

# IRCC sender signature (accent/OCR-tolerant; old releases print the name
# without a space, "ImmigrationRepresentatives").
_IRCC_SENDER_RE = re.compile(
    r"Immigration\s?Representatives"
    r"|R[eé]?pr?[eé]sentants?\s+imm?[a-z]*igration"
    r"|\(I?RCC\)",
    re.IGNORECASE,
)

# --- old-format fallback (releases without Archived: markers) ---------------
# Each email export starts with an Outlook header table: a From/Sent/To/Cc/
# Subject cluster with IRCC as the sender. OCR scrambles it (heading marks,
# From/Sent values swapped), but the cluster shape survives. Quoted question
# headers inside a thread lack Cc: or have an empty sender zone.
_OLD_FROM_RE = re.compile(r"(?:#+[ \t]*)?\bFrom[ \t]*:")
_TIME_OR_YEAR_RE = re.compile(r"\d{1,2}:\d{2}|\b\d{4}\b")

# Window sizes for old-format header-cluster detection, from observed OCR
# scatter in the real releases:
_SENT_WINDOW = 300  # Sent: must appear this close after From: in a real header
_HEADER_CLUSTER_SPAN = 450  # max observed OCR scatter of one header table

# Date-parsing windows around the first Sent: token.
# Forward covers the normal order ("Sent: Friday, November 21, 2025 ...");
# backward covers the OCR-swapped order, and is kept short enough never to
# reach an Archived: timestamp in new-format headers (>= ~82 chars away in
# real data).
_DATE_FWD_WINDOW = 120
_DATE_BACK_WINDOW = 60

_MONTHS = {
    m: i + 1
    for i, m in enumerate(
        "january february march april may june july august "
        "september october november december".split()
    )
}
_MONTHS_ABBR = {m[:3]: n for m, n in _MONTHS.items()}
_DATE_RE = re.compile(
    r"(January|February|March|April|May|June|July|August|September|October"
    r"|November|December)\s+(\d{1,2}),?\s+(\d{4})",
    re.IGNORECASE,
)

# RFC-style day-first form used by A-2025-13309 headers:
# "Sent: Tue, 1 Oct 2024 14:43:10" (abbreviated month, 24h time, no AM/PM).
_DATE_RFC_RE = re.compile(
    r"\b(\d{1,2})\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?,?\s+(\d{4})",
    re.IGNORECASE,
)

# Inline exchange labels inside a single IRCC reply (A-2025-13309 style):
# "Question 1", "Question:", "Answer:", "Response 1", "Question A)"; a bare
# capitalized word only counts when it is numbered, separated, or alone on a
# heading line (checked in _extract_inline_qa) so prose is never split.
_QA_LABEL_RE = re.compile(r"\b(Question|Answer|Response)\b[ \t]*(\d{1,2}|[A-D])?[ \t]*([:)])?")

# Leading [ \t]* (not \s*) so an empty header-table Subject: cell yields an
# empty value instead of swallowing the next body line.
_SUBJECT_RE = re.compile(
    r"Subject:[ \t]*(.*?)(?=\s*(?:Importance:|Sensitivity:|CAUTION\s*:|ATTENTION\s*:"
    r"|Archived:|\n|$))"
)

_PREFIX_RE = re.compile(r"^(?:re|fw|fwd|tr)\s*:\s*", re.IGNORECASE)

# Noise removed from question/answer bodies (kept verbatim in `raw`).
# The bilingual CAUTION banner is often interleaved by OCR, so each sentence
# fragment is stripped independently.
_NOISE_RES = [
    re.compile(p, re.IGNORECASE | re.DOTALL)
    for p in [
        r"<!--.*?-->",
        r"CAUTION\s*:\s*This email originated from outside the Government of\s+Canada\.?",
        r"Do not click on links or open",
        r"attachments unless you recognize the sender and know the content is\s+safe\.?",
        r"ATTENTION\s*:\s*Ce courriel provient de l\S{0,2}ext[ée]rieur du\s+gouvernement du Canada\.?",
        r"Ne cliquez pas sur les liens et",
        r"n\S{0,2}ouvrez pas les pi[èe]ces jointes sauf si vous reconnaissez\s+l\S{0,2}exp[ée]diteur et sachez que le contenu est s[ûu]r\.?",
        r"Information disclosed under the Access\s?to\s+Information Act",
        r"L\S*formation divulgu[ée]e en vertu de la \w+ sur \S*acc[èe]s [àa] \S+",
        r"Immigration,?\s+R[ée]fugi[ée]s",
        r"Immigration,?\s+Refugees",
        r"(?:and|et)\s+Cit[a-z]*yennet[ée]\s+Cana\w+",
        r"and\s+Cit[a-z]*zens?hip\s+Cana\w+",
        r"s\.\s?19\(1\)",
        # ATIP page stamps like 000041. Collateral: also eats legitimate
        # standalone 6-digit figures in body prose (rare); `raw` preserves them.
        r"(?<![\d-])\d{6}(?![\d-])",
    ]
]

# The quoted Subject: line inside a body, scrubbed FIRST — before the noise
# banners it often runs into (see _clean_body ordering).
_SUBJECT_SCRUB_RE = re.compile(
    r"Subject:\s*[^\n]{0,200}?(?=CAUTION\s*:|ATTENTION\s*:|Importance:|Sensitivity:|From:|\n|$)"
)

# Header fields scrubbed from bodies (OCR often glues them onto body lines).
# Case-sensitive on the field tokens so body words like "to"/"from" survive;
# bare "From"/"To" (colon lost to OCR) are only matched in known header shapes.
_HEADER_RES = [
    re.compile(p)
    for p in [
        r"Sent:\s*(?:\w+day,?\s*)?\w+\s+\d{1,2},?\s+\d{4},?\s*(?:at\s+)?\d{1,2}:\d{2}(?::\d{2})?\s*(?i:[AP]\.?M\.?)",
        # RFC day-first form (13309 headers; 10864 "Mail received time"):
        # "Sent: Tue, 1 Oct 2024 14:43:10" — 24h time, no AM/PM.
        r"(?:Sent|Mail received time):\s*(?:(?:Mon|Tue|Wed|Thu|Fri|Sat|Sun)[a-z]*,?\s*)?"
        r"\d{1,2}\s+\w{3,9}\.?,?\s+\d{4}(?:\s+\d{1,2}:\d{2}(?::\d{2})?)?",
        # Catch-all for OCR-mangled Sent dates ("201/", "Thursdav.", "PIVI"
        # for PM): anchored on a trailing time+meridian within 45 chars of
        # Sent:, so it can never consume real body content.
        r"Sent:[^\n]{0,45}?\d{1,2}[.:]\d{2}(?:[.:]\d{2})?\s*(?:[AP]\.?M\.?|PIVI|PIMI|AIVI|PIM|AVI|PV|AV)\b",
        r"Archived:\s*(?:\w+day,?\s*)?\w+\s+\d{1,2},?\s+\d{4},?\s*\d{1,2}:\d{2}(?::\d{2})?\s*(?i:[AP]\.?M\.?)",
        r"(?i:Immigration Representatives\s*/?\s*R[eé]\S*sentants?\s+im\w+igration\s*\(I?RCC\))",
        r"<?(?i:IRCC\.?ImmigrationRepresentatives)-?\s*",
        r"(?i:Representantsimmigration\.IRCC@cic\.gc\.ca)>?",
        r"<[^<>\s]{1,80}@[^<>\s]{1,80}>?",
        r"\bFrom\s*:,?\s*|\bFrom(?=\s+Sent:)",
        r"\bTo\s*:\s*|\bTo(?=\s+Cc:)",
        r"\bCc\s*:\s*",
        r"Importance:\s*\w+",
        r"Sensitivity:\s*\w+",
        r"\bImmigrationRepresentatives(?:@cic\.gc\.ca)?>?",
    ]
]

# Lines that are pure header residue after cleaning: a bare field token
# ("Sent:") or a lone date/time (From/Sent values scrambled loose by OCR).
# The date alternative requires the weekday comma ("Thursday, Auqust 24, ...")
# so wrapped prose lines like "on January 1, 2025" are never deleted; all
# observed real residue lines carry that comma.
_RESIDUE_LINE_RE = re.compile(
    r"^(?:(?:From|Sent|To|Cc|Subject|Importance|Sensitivity)\s*:?\s*)+$"
    r"|^\w+,\s+\w+\s+\d{1,2},?\s+\d{4}[\s\d:.,]*(?:[AP]\.?M\.?)?$"
    r"|^\w+,\s+\d{1,2}\s+\w{3,9}\.?,?\s+\d{4}[\s\d:.,]*$",
    re.IGNORECASE,
)


def normalize_subject(subject: str) -> str:
    """Strip repeated reply/forward prefixes (RE:/FW:/FWD:/TR:) and collapse whitespace."""
    s = re.sub(r"\s+", " ", subject).strip()
    while True:
        stripped = _PREFIX_RE.sub("", s, count=1)
        if stripped == s:
            break
        s = stripped.strip()
    return s


def _extract_subject(block: str) -> str:
    # Old-format header tables often carry an empty "Subject:" cell (the value
    # is displaced elsewhere by OCR) — take the first non-empty one.
    for m in _SUBJECT_RE.finditer(block):
        s = normalize_subject(m.group(1))
        if s:
            return s
    return ""


def _extract_date(block: str) -> str | None:
    """ISO date of the first Sent: header (newest email = the answer)."""
    idx = block.find("Sent:")
    if idx == -1:
        return None
    m = _DATE_RE.search(block, idx, idx + _DATE_FWD_WINDOW)
    if m:
        month, day = _MONTHS[m.group(1).lower()], m.group(2)
    else:
        rfc = _DATE_RFC_RE.search(block, idx, idx + _DATE_FWD_WINDOW)
        if rfc:  # day-first RFC style: "Sent: Tue, 1 Oct 2024 14:43:10"
            m, day = rfc, rfc.group(1)
            month = _MONTHS_ABBR[rfc.group(2).lower()]
        else:
            # Old-format OCR often swaps From/Sent values, leaving the date
            # just BEFORE the Sent: token.
            m = _DATE_RE.search(block, max(0, idx - _DATE_BACK_WINDOW), idx)
            if not m:
                return None
            month, day = _MONTHS[m.group(1).lower()], m.group(2)
    return f"{int(m.group(3)):04d}-{month:02d}-{int(day):02d}"


def _clean_body(text: str) -> str:
    text = _SUBJECT_SCRUB_RE.sub(" ", text)  # before banners: subjects run into them
    for rx in _NOISE_RES:
        text = rx.sub(" ", text)
    for rx in _HEADER_RES:
        text = rx.sub(" ", text)
    lines = []
    for line in text.splitlines():
        line = re.sub(r"^\s*#+\s*", "", line)  # OCR markdown headers = plain text
        line = re.sub(r"\s+", " ", line).strip()
        if not line or not re.search(r"[A-Za-zÀ-ÿ]{2}", line):
            continue  # empty or punctuation/stamp residue
        if _RESIDUE_LINE_RE.match(line):
            continue  # bare header token or a scrambled-loose date line
        lines.append(line)
    return "\n".join(lines).strip()


def _is_ircc_sender(segment: str) -> bool:
    """Classify a From-segment by the sender zone (between From and Sent:/To:/EOL)."""
    head = segment[:160].split("\n", 1)[0]
    for tok in ("Sent:", "To:", "Subject:"):
        cut = head.find(tok)
        if cut != -1:
            head = head[:cut]
    return bool(_IRCC_SENDER_RE.search(head))


def _extract_qa(block: str, first_is_answer: bool = False) -> tuple[str | None, str | None]:
    segments = _FROM_RE.split(block)
    answers: list[str] = []
    question: str | None = None
    for i, seg in enumerate(segments[1:]):  # segments[0] precedes the first From header
        body = _clean_body(seg)
        if not body:
            continue
        # In old-format exports the block starts at the IRCC reply's own header
        # (that's the boundary signal), so the first email is the answer even
        # when OCR scrambled the sender name out of the From: line.
        if (first_is_answer and i == 0) or _is_ircc_sender(seg):
            answers.append(body)
        elif question is None:
            question = body
    answer = "\n\n".join(answers) if answers else None
    if question is None and len(answers) == 1 and answer:
        # A-2025-13309 style: the quoted question email has no From: header;
        # IRCC's single reply inlines the exchange as labeled segments.
        inline = _extract_inline_qa(answer)
        if inline:
            return inline
    return question, answer


def _extract_inline_qa(body: str) -> tuple[str, str] | None:
    """Split an answer body carrying inline "Question .. Answer/Response .."
    labels into (question, answer). None unless BOTH sides come out non-empty
    (best-effort contract: never degrade an unlabeled body)."""
    marks = []
    for m in _QA_LABEL_RE.finditer(body):
        numbered, sep = m.group(2), m.group(3)
        line_start = body.rfind("\n", 0, m.start()) + 1
        line_end = body.find("\n", m.end())
        whole_line = (
            body[line_start:m.start()].strip("# ") == ""
            and body[m.end(): None if line_end == -1 else line_end].strip() == ""
        )
        # Keep real labels only: numbered ("Question 1"), separated
        # ("Answer:", "Question A)"), or a bare heading line ("### Question").
        if numbered or sep or whole_line:
            marks.append((m.start(), m.end(), m.group(1).lower()))
    questions, answers = [], []
    for (start, end, kind), nxt in zip(marks, marks[1:] + [(len(body), None, None)]):
        seg = body[end: nxt[0]].strip()
        if not seg:
            continue
        (questions if kind == "question" else answers).append(seg)
    if questions and answers:
        return "\n\n".join(questions), "\n\n".join(answers)
    return None


def _oldformat_boundaries(text: str) -> list[int]:
    """Start offsets of Outlook export header clusters in old-format text."""
    bounds = []
    for m in _OLD_FROM_RE.finditer(text):
        after = text[m.end(): m.end() + _HEADER_CLUSTER_SPAN]
        sent_at = after.find("Sent:")
        if not (0 <= sent_at <= _SENT_WINDOW) or "Cc:" not in after or "Subject:" not in after:
            continue
        # Sender zone must show IRCC or a swapped-in date; quoted question
        # headers ("From: Sent: ...") have an empty zone.
        zone = after[:sent_at]
        if not (_IRCC_SENDER_RE.search(zone) or _TIME_OR_YEAR_RE.search(zone)):
            continue
        bounds.append(m.start())
    return bounds


def _make_thread(block: str, first_is_answer: bool = False) -> dict:
    question, answer = _extract_qa(block, first_is_answer)
    return {
        "subject": _extract_subject(block),
        "date": _extract_date(block),
        "raw": block,
        "question": question,
        "answer": answer,
    }


def _split_oldformat_region(text: str) -> list[dict]:
    """Split a region of old-format exports at header clusters. Text before
    the first cluster (or a cluster-less region) is kept only with a Subject:
    header — otherwise it is a torn continuation tail."""
    threads: list[dict] = []
    bounds = _oldformat_boundaries(text)
    if not bounds:
        if "Subject:" in text:
            threads.append(_make_thread(text))
        return threads
    head = text[: bounds[0]]
    if head.strip() and "Subject:" in head:
        threads.append(_make_thread(head))
    for start, end in zip(bounds, bounds[1:] + [len(text)]):
        block = text[start:end]
        if block.strip():
            threads.append(_make_thread(block, first_is_answer=True))
    return threads


def split_threads(text: str) -> list[dict]:
    """Split raw OCR markdown into thread dicts, region-aware: Archived: email
    exports split first; regions between/before them that carry old-format
    header clusters are split by the old-format rules."""
    if not text or not text.strip():
        return []
    if not _ARCHIVED_RE.search(text):
        return _split_oldformat_region(text)
    parts = _ARCHIVED_RE.split(text)
    threads: list[dict] = []
    if parts[0].strip():
        # The pre-Archived head may itself be a whole old-format region
        # (mixed merged file) or just a torn continuation tail.
        threads.extend(_split_oldformat_region(parts[0]))
    for block in parts[1:]:
        if block.strip():
            # One Archived: export = one thread. Never re-split these by
            # old-format rules: long archived threads legitimately contain
            # several quoted IRCC reply headers (observed 6-deep chains) that
            # are indistinguishable from export header clusters.
            threads.append(_make_thread(block))
    return threads
