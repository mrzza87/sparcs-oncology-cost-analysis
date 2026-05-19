"""Formatting helpers for report-facing tables."""
from __future__ import annotations

import pandas as pd


def read_table(path: str) -> pd.DataFrame:
    """Read a CSV table using pandas."""
    return pd.read_csv(path)


def fmt_currency(value: float, digits: int = 0) -> str:
    """Format a number as a whole-dollar currency string."""
    return f"${value:,.{digits}f}"


def fmt_percent(value: float, digits: int = 1) -> str:
    """Format a proportion or percent value consistently.

    Values between 0 and 1 are treated as proportions. Values above 1 are treated as percentages.
    """
    if abs(value) <= 1:
        value = value * 100
    return f"{value:.{digits}f}%"


def ratio_to_percent_change(ratio: float, digits: int = 1) -> str:
    """Convert a multiplicative ratio into a percentage-change string."""
    change = (ratio - 1) * 100
    return f"{change:.{digits}f}%"
