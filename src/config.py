"""Path configuration for the SPARCS oncology cost analysis repository."""
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = REPO_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
OUTPUTS_DIR = REPO_ROOT / "outputs"
FINAL_TABLES_DIR = OUTPUTS_DIR / "final_tables"
SUPPORTING_TABLES_DIR = OUTPUTS_DIR / "supporting_tables"
FIGURES_DIR = OUTPUTS_DIR / "final_figures"
REPORT_ASSETS_DIR = OUTPUTS_DIR / "report_assets"
DOCS_DIR = REPO_ROOT / "docs"
