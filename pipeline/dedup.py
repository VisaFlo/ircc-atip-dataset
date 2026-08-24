"""Cross-release deduplication of parsed threads.

The dataset merges multiple ATIP releases whose date ranges overlap
(1A-2022-39382 spans 2017-01~2022-06 and overlaps A-2021-10864,
A-2021-10866 and 2A-2021-90643), so the same underlying email thread can
appear in two or more releases. Without dedup the public thread count is
inflated.

Two threads are considered duplicates iff their normalized subjects are
highly similar (difflib ratio > 0.9) and their dates fall within +/-3
days — or both dates are missing and the normalized subjects are exactly
equal. On merge the thread with the longer ``raw`` (more complete OCR)
wins, and ``atip_release`` becomes the sorted list of every contributing
release. Stdlib only; no third-party deps.
"""
from __future__ import annotations

import re
from datetime import date as _date
from difflib import SequenceMatcher

_SIMILARITY_THRESHOLD = 0.9
_DATE_WINDOW_DAYS = 3

# Subjects arrive already RE:/FW:-normalized by the splitter; for comparison
# we additionally casefold and strip punctuation/whitespace noise (OCR often
# mangles commas, dashes and spacing).
_PUNCT_RE = re.compile(r"[^\w\s]+")
_WS_RE = re.compile(r"\s+")


def _norm_subject(subject: str | None) -> str:
    s = _PUNCT_RE.sub(" ", (subject or "").casefold())
    return _WS_RE.sub(" ", s).strip()


def _parse_date(value: str | None) -> _date | None:
    if not value:
        return None
    try:
        return _date.fromisoformat(value)
    except ValueError:
        return None


def _similar(a: str, b: str) -> bool:
    if a == b:
        return True
    la, lb = len(a), len(b)
    if not la or not lb:
        return False
    # Cheap length-band prefilter: SequenceMatcher.ratio() can never exceed
    # 2*min(la,lb)/(la+lb), so skip the O(n*m) pass when that bound already
    # fails the threshold.
    if 2 * min(la, lb) / (la + lb) <= _SIMILARITY_THRESHOLD:
        return False
    return SequenceMatcher(None, a, b).ratio() > _SIMILARITY_THRESHOLD


def _releases(thread: dict) -> list[str]:
    r = thread.get("atip_release")
    if r is None:
        return []
    if isinstance(r, list):
        return list(r)
    return [r]


def dedup(threads: list[dict]) -> list[dict]:
    """Collapse cross-release duplicate threads.

    Returns new dicts (inputs are not mutated). Every output thread carries
    ``atip_release`` as a sorted list[str] of contributing releases (empty
    if no input carried one).
    """
    n = len(threads)
    parent = list(range(n))

    def find(x: int) -> int:
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a: int, b: int) -> None:
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra

    norms = [_norm_subject(t.get("subject")) for t in threads]
    dates = [_parse_date(t.get("date")) for t in threads]

    # --- dated threads: sort by date, compare only within the +/-3-day
    # sliding window so comparisons stay local instead of O(n^2).
    dated = sorted(
        ((d.toordinal(), i) for i, d in enumerate(dates) if d is not None),
    )
    lo = 0
    for k, (ordinal, i) in enumerate(dated):
        while dated[lo][0] < ordinal - _DATE_WINDOW_DAYS:
            lo += 1
        if not norms[i]:
            continue  # never merge threads whose subject is empty/unreadable
        for j in range(lo, k):
            jj = dated[j][1]
            if find(i) == find(jj):
                continue
            if _similar(norms[i], norms[jj]):
                union(i, jj)

    # --- undated threads: merge only on exact normalized-subject equality,
    # bucketed by subject so lookup is O(1).
    undated_buckets: dict[str, int] = {}
    for i, d in enumerate(dates):
        if d is not None or not norms[i]:
            continue
        first = undated_buckets.setdefault(norms[i], i)
        if first != i:
            union(first, i)

    # --- emit: one thread per cluster, ordered by first appearance.
    clusters: dict[int, list[int]] = {}
    for i in range(n):
        clusters.setdefault(find(i), []).append(i)

    out: list[dict] = []
    for members in sorted(clusters.values(), key=lambda m: m[0]):
        winner = max(members, key=lambda i: len(threads[i].get("raw") or ""))
        merged = dict(threads[winner])
        merged["atip_release"] = sorted(
            {r for i in members for r in _releases(threads[i])}
        )
        out.append(merged)
    return out
