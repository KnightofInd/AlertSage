# LLM Integration

## Overview

The project uses **llama.cpp** for privacy-first local LLM inference in two key areas:

1. **Dataset Generation** - Enhancing synthetic narratives
2. **Second-Opinion Triage** - Assisting with uncertain classifications

## Setup

### Install llama-cpp-python

```bash
# For Apple Silicon (Metal acceleration)
CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python

# For CUDA GPUs
CMAKE_ARGS="-DLLAMA_CUDA=on" pip install llama-cpp-python

# CPU only
pip install llama-cpp-python
```

### Download Model

Recommended: Llama-2-7B-Chat (Q5_K_S quantization)

```bash
wget https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGUF/resolve/main/llama-2-7b-chat.Q5_K_S.gguf \
  -P models/
```

### Configure Environment

```bash
export TRIAGE_LLM_MODEL=$(pwd)/models/llama-2-7b-chat.Q5_K_S.gguf
export TRIAGE_LLM_DEBUG=1
```

## Dataset Generation

### Enable LLM Rewriting

```bash
python generator/generate_cyber_incidents.py \
  --n-events 5000 \
  --use-llm \
  --rewrite-report audit.json
```

### Rewrite Parameters

```bash
export NLP_TRIAGE_LLM_REWRITE_PROB=0.30  # 30% of incidents rewritten
export NLP_TRIAGE_LLM_TEMPERATURE=0.2     # Focused generation
export NLP_TRIAGE_LLM_MAX_RETRIES=3       # Error recovery
```

### How It Works

1. Generator creates baseline narrative
2. LLM probabilistically rewrites (30% by default)
3. Sanitization removes artifacts
4. Validation ensures quality
5. Audit log tracks statistics

## Second-Opinion Triage

### CLI Usage

```bash
# Single incident
nlp-triage --llm-second-opinion "Suspicious activity detected"

# Bulk processing
nlp-triage --llm-second-opinion \
  --input-file incidents.txt \
  --output-file results.jsonl
```

### Streamlit UI

Enable "LLM Second Opinion" toggle in the sidebar.

### Guardrails

The second-opinion engine includes multiple safety layers:

1. **JSON Parsing** - Structured output validation
2. **SOC Keyword Intelligence** - Domain-specific validation
3. **Label Normalization** - Maps variations to canonical labels
4. **Confidence Filtering** - Only engages on uncertain cases
5. **Timeout Protection** - Prevents hanging on bad inputs

## Advanced Configuration

### Model Parameters

```bash
# Context window (tokens)
export TRIAGE_LLM_CTX=4096

# Max generation tokens
export TRIAGE_LLM_MAX_TOKENS=512

# Temperature (creativity)
export TRIAGE_LLM_TEMP=0.2

# Top-p sampling
export TRIAGE_LLM_TOP_P=0.9
```

### Backend Selection

```bash
# Absolute path to model
export NLP_TRIAGE_LLM_BACKEND=/full/path/to/model.gguf
```

## Performance Tuning

### CPU Optimization

```bash
# Increase thread count
export OMP_NUM_THREADS=8

# Use BLAS
CMAKE_ARGS="-DLLAMA_BLAS=ON" pip install llama-cpp-python
```

### GPU Acceleration

```bash
# CUDA
CMAKE_ARGS="-DLLAMA_CUDA=on" pip install llama-cpp-python

# Metal (Apple Silicon)
CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python
```

### Memory Management

```bash
# Reduce context for lower memory
export TRIAGE_LLM_CTX=2048

# Use quantized models (Q4, Q5)
# Smaller = less accurate but faster
```

## Troubleshooting

### Import Errors

```bash
# Reinstall with correct flags
pip uninstall llama-cpp-python
CMAKE_ARGS="-DLLAMA_METAL=on" pip install llama-cpp-python
```

### Slow Inference

- Use quantized models (Q5_K_S recommended)
- Enable GPU acceleration
- Reduce context window
- Lower max tokens

### Out of Memory

- Use smaller model (7B instead of 13B)
- Reduce context window
- Close other applications

### Debug Mode

```bash
export TRIAGE_LLM_DEBUG=1
nlp-triage --llm-second-opinion "test incident"
```

## Best Practices

✅ Use quantized models (Q5_K_S or Q4_K_M)  
✅ Enable GPU acceleration when available  
✅ Set appropriate context window for your RAM  
✅ Monitor resource usage during generation  
✅ Use lower temperature for focused outputs  
✅ Enable debug mode for troubleshooting

❌ Don't use unquantized models (too large)  
❌ Don't set context > 8192 without sufficient RAM  
❌ Don't ignore timeout warnings  
❌ Don't disable guardrails in production

---

See [Production Generation](production-generation.md) for monitoring LLM-enhanced dataset creation.
