# Development

This page captures the day-to-day workflow for contributing changes, running tests, and keeping artifacts aligned with the codebase.

---

## Environment & installation

- Python **3.11+** is required (see `pyproject.toml`).
- Install the package in editable mode with dev extras:

```bash
pip install -e ".[dev]"
```

  This exposes the `nlp-triage` console script, installs `pytest`, and pulls in the runtime stack (`scikit-learn`, `pandas`, `rich`, etc.).

- Optional: if you prefer an isolated environment, create a `.venv` before installing (documented on the [Getting Started](getting-started.md) page).

---

## Tests & continuous integration

Pytest lives in `tests/` and exercises the three main building blocks:

| Test module | Focus area |
| --- | --- |
| `tests/test_preprocess.py` | Deterministic text cleaning rules (`triage.preprocess.clean_description`) |
| `tests/test_model_artifacts.py` | Ensures the saved TF–IDF + Logistic Regression artifacts exist and can predict |
| `tests/test_cli.py` | Verifies CLI helpers return the expected prediction payload structure |

Run the entire suite with:

```bash
pytest
```

CI simply mirrors this command. Keep artifacts (`models/vectorizer.joblib`, `models/baseline_logreg.joblib`) in sync with the dataset to avoid false negatives.

---

## Local CLI + notebook checks

- **CLI sanity check** after making pipeline changes:

```bash
nlp-triage "Employee forwarded an email that spoofs the VPN login page."
```

    Use `--threshold` and `--json` to stress uncertainty logic or automation scenarios (`docs/cli.md` dives deeper).

- **Notebook reproducibility**:
  - Run notebooks in order on the latest CSV to regenerate metrics and visuals (`docs/notebooks.md` lists the flow).
  - Commit regenerated artifacts when you intentionally change training code; otherwise avoid stale diffs by reusing existing models/vectorizers.

---

## Documenting and serving the docs

- All user-facing documentation lives in `docs/` and is wired up via `mkdocs.yml`.
- Preview local changes with:

```bash
mkdocs serve
```

  (MkDocs Material is declared in `requirements.txt`; install it if you plan to live-preview docs.)

---

## Re-generating data or models

1. Regenerate datasets via `generator/generate_cyber_incidents.py` (details on [Data & Synthetic Generator](data-and-generator.md)).
2. Retrain models in `notebooks/03_baseline_model.ipynb` (and optional comparison notebooks).
3. Copy the resulting `vectorizer.joblib` and `baseline_logreg.joblib` into `models/` so the CLI and tests pick them up.

Whenever one of these steps changes, re-run `pytest` to ensure inference helpers still behave as expected.
