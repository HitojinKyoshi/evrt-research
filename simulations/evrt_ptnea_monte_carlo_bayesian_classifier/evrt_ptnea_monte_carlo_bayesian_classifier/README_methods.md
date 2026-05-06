# EVRT/PTNEA Monte Carlo + Bayesian Artifact Classifier

This package contains a synthetic Monte Carlo simulation and Bayesian-style classifier for
artifact discrimination in PTNEA / EVRT residual-force experiments.

## Purpose

The goal is to test whether correlated multi-domain diagnostic behavior can distinguish:

- EHD / plasma artifacts
- thermal lag artifacts
- Lorentz / RF cable artifacts
- mechanical vibration artifacts
- mixed artifacts
- residual candidates
- null experiments

## Important limitation

This is a synthetic reduced-order diagnostic model. It is not evidence for anomalous propulsion,
not a finite-element solver, and not trained on real experimental data.

## Dataset

Total synthetic experiments: 7000
Experiments per class: 1000

## Diagnostic features

- pressure_survival
- geometry_reversal
- dummy_suppression
- thermal_lag_score
- resonance_alignment
- cable_sensitivity
- repeatability
- snr
- phase_promptness

## Bayesian classifier

The classifier uses a Gaussian naive-Bayes likelihood model based on assumed diagnostic signatures.
The output includes posterior probabilities for each source class and residual-candidate thresholds.

## Key outputs

- `data/monte_carlo_bayesian_classifier_full_dataset.csv`
- `data/confusion_matrix_counts.csv`
- `data/confusion_matrix_normalized.csv`
- `data/residual_candidate_threshold_performance.csv`
- `data/feature_separation_residual_vs_nonresidual.csv`
- `figures/confusion_matrix_heatmap.png`
- `figures/posterior_residual_distributions.png`
- `figures/diagnostic_feature_separation.png`
- `summary_results.json`
