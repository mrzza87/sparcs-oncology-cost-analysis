"""Cohort-definition notes for the primary cancer analysis.

The full cohort construction is implemented in the notebooks. This module records the report-facing
classification logic used across the evidence pack.
"""

PRIMARY_CANCER_COHORT_LABEL = "primary_cancer"
BROADER_CANCER_RELATED_LABEL = "broader_cancer_related"
NON_CANCER_LABEL = "non_cancer"

HAEMATOLOGIC_CANCER_KEYWORDS = (
    "LEUKEMIA",
    "LYMPHOMA",
    "MYELOMA",
)


def is_haematologic_cancer(description: str) -> bool:
    """Return True if a CCSR diagnosis description maps to the report-facing haematologic group."""
    text = str(description).upper()
    return any(keyword in text for keyword in HAEMATOLOGIC_CANCER_KEYWORDS)
