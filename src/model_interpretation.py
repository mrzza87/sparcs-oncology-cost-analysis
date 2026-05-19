"""Small helpers for interpreting ratio-scale model outputs."""
from __future__ import annotations


def ratio_direction(ratio: float) -> str:
    """Return a plain-language direction for ratio-scale model estimates."""
    if ratio > 1:
        return "higher"
    if ratio < 1:
        return "lower"
    return "no difference"


def ci_excludes_one(lower: float, upper: float) -> bool:
    """Return True when a ratio-scale 95% confidence interval excludes 1.0."""
    return upper < 1 or lower > 1
