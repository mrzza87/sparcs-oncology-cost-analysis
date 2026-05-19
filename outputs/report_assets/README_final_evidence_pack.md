# Final Evidence Pack

## Project

Cancer-related inpatient utilisation and cost variation using SPARCS administrative discharge data.

## Created

2026-05-16T13:56:42

## Folder structure

- `outputs/final_tables/`: selected tables for the final report and evidence pack.
- `outputs/final_figures/main_report/`: selected figures for the main report.
- `outputs/final_figures/diagnostics_appendix/`: diagnostic and sensitivity figures.
- `outputs/report_assets/`: inventories, master summary and final model effects summary.

## Final modelling strategy

The final report should use:

1. Negative Binomial GLM for length of stay.
2. Gamma GLM with log link for total inpatient costs.
3. Logistic GLM for high-cost admission status.

The Poisson LOS model and log-linear OLS cost model are retained only as diagnostic or sensitivity outputs.

## Main report model figures

- `08_final_negative_binomial_los_model_irr.png`
- `09_final_gamma_cost_model_cost_ratios.png`
- `10_final_high_cost_logistic_model_odds_ratios.png`

## Do not use

The following old duplicate figures should not be used in the report:

- `notebook_05_cost_model_cost_ratios.png`
- `notebook_05_los_model_incidence_rate_ratios.png`

## Key report assets

- `master_summary_table.csv`
- `final_model_effects_summary.csv`
- `table_inventory.csv`
- `figure_inventory.csv`
- `final_report_figure_shortlist.csv`
- `final_evidence_manifest.json`
