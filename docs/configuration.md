# Configuration

## Environment Variables

### LLM Configuration

```bash
# Model path
export TRIAGE_LLM_MODEL=/path/to/llama-2-7b-chat.Q5_K_S.gguf

# Generation settings
export NLP_TRIAGE_LLM_GENERATOR=1
export NLP_TRIAGE_LLM_REWRITE_PROB=0.30
export NLP_TRIAGE_LLM_TEMPERATURE=0.2
export NLP_TRIAGE_LLM_MAX_RETRIES=3

# Debugging
export TRIAGE_LLM_DEBUG=1
```

### Model Settings

```bash
# Context window
export TRIAGE_LLM_CTX=4096

# Max tokens for generation
export TRIAGE_LLM_MAX_TOKENS=512

# Temperature (0.0-1.0)
export TRIAGE_LLM_TEMP=0.2
```

## CLI Configuration

### Uncertainty Thresholds

```bash
# Default threshold
nlp-triage --threshold 0.50 "incident text"

# High confidence mode
nlp-triage --threshold 0.70 "incident text"

# Low confidence mode
nlp-triage --threshold 0.30 "incident text"
```

### Difficulty Modes

- `default` - Standard uncertainty handling
- `soc-medium` - Moderate strictness
- `soc-hard` - Maximum strictness for edge cases

## Streamlit UI Configuration

The UI respects the same environment variables as the CLI.

## Dataset Generation

### Generation Parameters

```python
# In generate_cyber_incidents.py
--n-events 50000           # Number of incidents
--chunk-size 1000          # Checkpointing frequency
--start-date 2024-01-01    # Date range start
--end-date 2024-12-31      # Date range end
--use-llm                  # Enable LLM rewriting
--rewrite-report audit.json # LLM statistics output
```

See [Production Generation](production-generation.md) for details.
