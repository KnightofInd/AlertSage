# Modeling & Evaluation

## Text Representation

The baseline models use **TF–IDF** over cleaned incident descriptions:

- Unigrams + bigrams
- English stopword removal
- `min_df` and `max_df` thresholds to drop extremely rare / frequent terms
- Max feature cap (e.g., 5,000 terms)

Cleaning is shared between training and inference via `triage.preprocess.clean_description`.

---

## Models compared

Notebook **08_Model_Comparison** trains and compares several models:

- `logreg_baseline` — Logistic Regression (multi-class, one-vs-rest)
- `linear_svm` — Linear SVM classifier
- `random_forest` — Random Forest over TF–IDF features

On the synthetic test set (~20k rows), these models all achieve around **92% accuracy**, with:

- High precision/recall for clear-cut classes (`phishing`, `malware`, `web_attack`, `data_exfiltration`)
- Lower but still strong performance on more ambiguous narratives (`benign_activity`, overlapping `policy_violation` scenarios)

---

## Scenario-based evaluation

Notebook **07_Scenario_Based_Evaluation**:

- Tests the model on **hand-crafted narratives** that look like real tickets or alerts
- Compares **expected event_type** vs **model prediction**
- Surfaces realistic errors:
  - Some benign operations labeled as `web_attack` or `policy_violation`
  - Some policy violations near data movement labeled as `data_exfiltration`
  - Borderline authentication issues split between `access_abuse` and `benign_activity`

This helps validate that the model is learning **semantically meaningful patterns** rather than just memorizing templates.

---

## Training artifacts & reproducibility

- Notebooks **02–04** export `models/vectorizer.joblib` and `models/baseline_logreg.joblib`.
- `triage.model.load_vectorizer_and_model()` (used by the CLI and tests) expects those filenames, so keep them consistent.
- To experiment with alternate classifiers, either:
  - Update `notebooks/08_model_comparison.ipynb` and drop extra `.joblib` files next to the baseline, or
  - Edit `src/triage/model.py` / `src/triage/cli.py` to point at the new artifact names.
- The CLI always calls `predict_proba`, so stick to classifiers that expose that method or wrap them with `CalibratedClassifierCV`.

---

## Takeaways

- TF–IDF + simple linear models can perform **surprisingly well** on structured, synthetic incident narratives.
- For real SOC deployment, you would likely:
  - Incorporate **structured features** (severity, log source, time of day, etc.)
  - Move to **transformer-based embeddings**
  - Tighten evaluation on **true production tickets**

When experimenting, rerun the `pytest` suite to confirm the refreshed artifacts still contain the expected class labels.
