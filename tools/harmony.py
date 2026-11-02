"""Chord names from the pitches actually present.

The quality is the interval set above the declared root. A missing fifth stays
out of the name only when the remaining intervals are an entry in this table.
"""

from __future__ import annotations

QUALITIES = {
    frozenset({0, 2, 3, 10}): "m9",
    frozenset({0, 2, 3, 7, 10}): "m9",
    frozenset({0, 2, 4, 11}): "maj9",
    frozenset({0, 2, 4, 7, 11}): "maj9",
    frozenset({0, 2, 4, 10}): "9",
    frozenset({0, 2, 4, 7, 10}): "9",
    frozenset({0, 3, 4, 10}): "7#9",
    frozenset({0, 3, 4, 7, 10}): "7#9",
    frozenset({0, 4, 9, 10}): "13",
    frozenset({0, 4, 7, 9, 10}): "13",
    frozenset({0, 2, 4, 9, 10}): "13",
    frozenset({0, 3, 5, 10}): "m11",
    frozenset({0, 3, 5, 7, 10}): "m11",
    frozenset({0, 3, 7, 10}): "m7",
    frozenset({0, 3, 10}): "m7",
    frozenset({0, 4, 7, 11}): "maj7",
    frozenset({0, 4, 11}): "maj7",
    frozenset({0, 4, 7, 10}): "7",
    frozenset({0, 4, 10}): "7",
    frozenset({0, 1, 4, 10}): "7b9",
    frozenset({0, 1, 4, 7, 10}): "7b9",
}


def chord_name(root_pc: int, pitches: list[int], spelling: list[str]) -> str:
    intervals = frozenset((pitch - root_pc) % 12 for pitch in pitches)
    quality = QUALITIES.get(intervals)
    if quality is None:
        raise ValueError(
            f"unnamed chord root {spelling[root_pc]} intervals {sorted(intervals)} pitches {pitches}"
        )
    return spelling[root_pc] + quality


def spell_pitch(pitch: int, spelling: list[str]) -> str:
    return f"{spelling[pitch % 12]}{pitch // 12 - 1}"
