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

Semantics worth knowing:

* Clustering is a **transitive closure** (union-find): if A~B and B~C,
  all three collapse into one thread even when A and C alone would not
  match (e.g. their dates are 5 days apart). For a daily re-send chain
  this is what you want; it can over-collapse a long chain of near-daily
  identical subjects.
* **Within-release duplicates merge too** — intended. Some packages OCR
  the same thread twice; those are just as much duplicates as
  cross-release copies (their ``atip_release`` list then has one entry).
* Registrar **tracking stamps** appended to subjects ("- REP-B-2025-1767
  - Due 21-Oct-25") are stripped from the *comparison* subject only (the
  output keeps the original). But a REP id is also evidence: two clusters
  that carry *different* REP id sets are never merged, even when their
  stripped subjects are identical — id inequality is positive evidence
  of distinct threads, and an unstamped copy cannot bridge them.
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

# Registrar tracking stamps appended to subjects, e.g.
# "... - REP-B-2025-1767 - Due 21-Oct-25". Matched on the casefolded
# subject with flexible separators (OCR turns hyphens into spaces).
_REP_ID_RE = re.compile(
    r"\brep[\s\-–—:#]*(?:([a-z])[\s\-]+)?(\d{4})[\s\-]+(\d{4})\b"
)
_DUE_RE = re.compile(r"\bdue[\s\-:]*\d{1,2}[\s\-][a-z]{3,9}\.?[\s\-,]*\d{2,4}\b")


def _normalize(subject: str | None) -> tuple[str, frozenset[str]]:
    """Return (comparison subject, REP ids found in it).

    Tracking stamps and Due fragments are stripped from the comparison
    string; the extracted REP ids feed the distinctness guard.
    """
    s = (subject or "").casefold()
    ids = frozenset(
        "-".join(g for g in m.groups() if g) for m in _REP_ID_RE.finditer(s)
    )
    s = _REP_ID_RE.sub(" ", s)
    s = _DUE_RE.sub(" ", s)
    s = _PUNCT_RE.sub(" ", s)
    return _WS_RE.sub(" ", s).strip(), ids


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

    normed = [_normalize(t.get("subject")) for t in threads]
    norms = [nm for nm, _ in normed]
    # REP ids per *cluster* root: the guard is cluster-level so an unstamped
    # thread that joined an id-bearing cluster inherits its ids and cannot
    # later bridge to a cluster with different ids.
    cluster_ids: dict[int, frozenset[str]] = {
        i: ids for i, (_, ids) in enumerate(normed)
    }

    def try_union(a: int, b: int) -> None:
        ra, rb = find(a), find(b)
        if ra == rb:
            return
        ids_a, ids_b = cluster_ids[ra], cluster_ids[rb]
        if ids_a and ids_b and ids_a != ids_b:
            return  # different REP ids: positive evidence of distinctness
        parent[rb] = ra
        cluster_ids[ra] = ids_a | ids_b

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
                try_union(i, jj)

    # --- undated threads: merge only on exact normalized-subject equality,
    # bucketed by subject so lookup is O(1) (the REP-id guard still applies
    # inside a bucket via try_union).
    undated_buckets: dict[str, list[int]] = {}
    for i, d in enumerate(dates):
        if d is not None or not norms[i]:
            continue
        bucket = undated_buckets.setdefault(norms[i], [])
        for j in bucket:
            try_union(j, i)
        bucket.append(i)

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
