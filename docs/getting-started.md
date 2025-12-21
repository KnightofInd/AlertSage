# Getting Started

Follow these steps to install the project locally, run the CLI, and confirm everything is wired correctly.

---

## Prerequisites

- Python **3.11 or newer**
- Git
- (Recommended) A virtual environment tool such as `venv`

---

## 1. Clone the repository

```bash
git clone https://github.com/texasbe2trill/AlertSage.git
cd AlertSage
```

---

## 2. Create & activate a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # macOS / Linux
# .venv\Scripts\activate   # Windows PowerShell
```

Any Python env tool works; `.venv` just keeps dependencies isolated from your system install.

---

## 3. Install the package (with dev extras)

```bash
pip install -e ".[dev]"
```

This editable install exposes the `nlp-triage` CLI and pulls dev dependencies (Pytest) listed in `pyproject.toml`.

---

## 4. Verify model artifacts + CLI

Models and vectorizer are stored in:

```
models/
├── vectorizer.joblib
└── baseline_logreg.joblib
```

Quick confidence checks:

```bash
# Ensure artifacts load without errors
python -c "from triage.model import load_vectorizer_and_model; print(load_vectorizer_and_model()[0].__class__)"

# Run a single-shot CLI prediction
nlp-triage "User reported a suspicious payroll login email with a fake link."
```

For JSON output (useful for automation testing):

```bash
nlp-triage --json "VPN portal prompted for re-authentication and asked for MFA reset."
```

Screenshots of the formatted output live in `docs/images/`.

---

## 5. Run the unit tests

```bash
pytest
```

See [Development](development.md) for a breakdown of what each test covers.

---

## Optional next steps

- **Regenerate data** via `python generator/generate_cyber_incidents.py` (details on [Data & Synthetic Generator](data-and-generator.md)).
- **Explore notebooks** under `notebooks/` to retrace the modeling workflow.
- **Preview docs** while editing by running `mkdocs serve`.
