# API Reference

!!! info "Coming Soon"
Comprehensive API documentation is being developed.

## Core Modules

### `triage.preprocess`

```python
from triage.preprocess import clean_description

clean_text = clean_description("URGENT!!! Login FAILED!!!")
# Returns: "urgent login failed"
```

### `triage.model`

```python
from triage.model import load_vectorizer_and_model, predict_event_type

vectorizer, classifier = load_vectorizer_and_model()
label, probabilities = predict_event_type("Suspicious payroll login email")
```

### `triage.cli`

See [CLI Usage](cli.md) for command-line interface documentation.

## Function Reference

### Text Processing

#### `clean_description(text: str) -> str`

Cleans and normalizes incident text.

**Parameters:**

- `text` (str): Raw incident description

**Returns:**

- str: Cleaned text (lowercase, normalized)

### Model Loading

#### `load_vectorizer_and_model() -> Tuple[Vectorizer, Classifier]`

Loads the saved TF–IDF vectorizer and trained classifier used by the CLI.

**Returns:**

- Tuple: `(vectorizer, classifier)` objects ready for inference

### Inference

#### `predict_event_type(text: str, top_k: int = 5) -> Tuple[str, Optional[Dict[str, float]]]`

Predicts the most likely incident label and (optionally) a top-k probability breakdown.

**Parameters:**

- `text` (str): Incident description
- `top_k` (int): Maximum classes to include in the probability dict

**Returns:**

- Tuple: `(label, probabilities)` where `label` is a string and `probabilities` is an optional dict of class → probability

## Data Structures

### Prediction Result

Programmatic API returns a tuple. For a structured payload, use the CLI with `--json`.

## CLI Integration

For programmatic usage, use JSON mode:

```python
import subprocess
import json

result = subprocess.run(
    ["nlp-triage", "--json", "incident text"],
    capture_output=True,
    text=True
)

prediction = json.loads(result.stdout)
```

---

For usage examples, see [Notebooks Overview](notebooks.md).
