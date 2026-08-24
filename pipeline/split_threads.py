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
# "From:", "From:,", "From Sent:" (colon lost).
_FROM_RE = re.compile(r"(?=\bFrom:)|(?=\bFrom,?\s+Sent:)")

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
_OLD_FROM_RE = re.compile(r"(?:#+\s*)?\bFrom\s*:")
_TIME_OR_YEAR_RE = re.compile(r"\d{1,2}:\d{2}|\b\d{4}\b")

_MONTHS = {
    m: i + 1
    for i, m in enumerate(
        "january february march april may june july august "
        "september october november december".split()
    )
}
_DATE_RE = re.compile(
    r"(January|February|March|April|May|June|July|August|September|October"
    r"|November|December)\s+(\d{1,2}),?\s+(\d{4})",
    re.IGNORECASE,
)

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
        r"(?<![\d-])\d{6}(?![\d-])",  # ATIP page stamps like 000041
    ]
]

# Header fields scrubbed from bodies (OCR often glues them onto body lines).
# Case-sensitive on the field tokens so body words like "to"/"from" survive;
# bare "From"/"To" (colon lost to OCR) are only matched in known header shapes.
_HEADER_RES = [
    re.compile(p)
    for p in [
        r"Subject:\s*[^\n]{0,200}?(?=CAUTION\s*:|ATTENTION\s*:|Importance:|Sensitivity:|From:|\n|$)",
        r"Sent:\s*(?:\w+day,?\s*)?\w+\s+\d{1,2},?\s+\d{4},?\s*(?:at\s+)?\d{1,2}:\d{2}(?::\d{2})?\s*(?i:[AP]\.?M\.?)",
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
_RESIDUE_LINE_RE = re.compile(
    r"^(?:(?:From|Sent|To|Cc|Subject|Importance|Sensitivity)\s*:?\s*)+$"
    r"|^\w+,?\s+\w+\s+\d{1,2},?\s+\d{4}[\s\d:.,]*(?:[AP]\.?M\.?)?$",
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
    m = _DATE_RE.search(block, idx, idx + 120)
    if not m:
        # Old-format OCR often swaps From/Sent values, leaving the date just
        # BEFORE the Sent: token. (60 chars is too short to reach back to the
        # Archived: timestamp in new-format headers.)
        m = _DATE_RE.search(block, max(0, idx - 60), idx)
    if not m:
        return None
    month = _MONTHS[m.group(1).lower()]
    return f"{int(m.group(3)):04d}-{month:02d}-{int(m.group(2)):02d}"


def _clean_body(text: str) -> str:
    for rx in _HEADER_RES[:1]:  # Subject line first, before banner removal
        text = rx.sub(" ", text)
    for rx in _NOISE_RES:
        text = rx.sub(" ", text)
    for rx in _HEADER_RES[1:]:
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
    return question, answer


def _oldformat_boundaries(text: str) -> list[int]:
    """Start offsets of Outlook export header clusters in old-format text."""
    bounds = []
    for m in _OLD_FROM_RE.finditer(text):
        after = text[m.end(): m.end() + 450]
        sent_at = after.find("Sent:")
        if not (0 <= sent_at <= 300) or "Cc:" not in after or "Subject:" not in after:
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


def split_threads(text: str) -> list[dict]:
    """Split raw OCR markdown into thread dicts (one per Archived: email export)."""
    if not text or not text.strip():
        return []
    threads: list[dict] = []
    if _ARCHIVED_RE.search(text):
        parts = _ARCHIVED_RE.split(text)
        # Text before the first Archived: marker is a continuation tail from a
        # previous chunk — keep it only if it carries a Subject: header.
        head = parts[0]
        if head.strip() and "Subject:" in head:
            threads.append(_make_thread(head))
        for block in parts[1:]:
            if block.strip():
                threads.append(_make_thread(block))
        return threads
    # Old-format fallback: no Archived: markers; split at export header
    # clusters. Each export leads with the IRCC reply.
    bounds = _oldformat_boundaries(text)
    if not bounds:
        # No boundaries at all: a lone torn block is kept only with a Subject:.
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
