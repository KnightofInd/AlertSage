# Testing Guide

## Test Structure

Tests are organized in the `tests/` directory:

```
tests/
├── test_cli.py          # CLI functionality tests
├── test_model.py        # Model loading and inference
├── test_preprocess.py   # Text preprocessing
└── conftest.py          # Shared fixtures
```

## Running Tests

### All Tests

```bash
pytest tests/ -v
```

### Specific Test File

```bash
pytest tests/test_cli.py -v
```

### Specific Test Function

```bash
pytest tests/test_cli.py::test_basic_classification -v
```

### With Coverage

```bash
pytest tests/ --cov=src/triage --cov-report=html
```

## Writing Tests

### Example Test

```python
import pytest
from triage.preprocess import clean_description

def test_clean_description():
    dirty = "URGENT!!! Multiple LOGIN failures!!!"
    clean = clean_description(dirty)
    assert clean == "urgent multiple login failures"
    assert "!!!" not in clean
```

### Using Fixtures

```python
@pytest.fixture
def sample_incident():
    return "User reported suspicious email with attachment"

def test_classification(sample_incident):
    result = classify_incident(sample_incident)
    assert result["label"] in ["phishing", "malware", "uncertain"]
```

## Test Categories

### Unit Tests

- Individual function testing
- No external dependencies
- Fast execution

### Integration Tests

- Multiple component interaction
- Model loading and inference
- CLI end-to-end workflows

### Dataset Tests

- Automatic dataset download
- Checkpoint loading
- CSV validation

## Continuous Integration

Tests run automatically on:

- Pull requests to `main` or `dev`
- Pushes to `main` or `dev`

See `.github/workflows/python-tests.yml` for configuration.

---

See [Development Guide](development.md) for more development workflows.
