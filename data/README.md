# Data availability

The row-level SPARCS extract and processed admission-level datasets are intentionally not included in this public repository.

This repository contains only aggregated report tables, figures, notebooks, and documentation needed to review the analytical workflow and final findings. To reproduce the full analysis from raw data, obtain the relevant SPARCS 2024 inpatient discharge extract from the public source cited in the report, place it under `data/raw/`, and run the notebooks in order.

Expected local path if reproducing from raw data:

```text
data/raw/sparcs_2024_extract_50000.csv
```

The report findings in this repository are based on a cleaned 50,000-record inpatient extract and a primary cancer analysis cohort of 1,218 admissions.
