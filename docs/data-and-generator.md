# Data & Synthetic Generator

Understanding the dataset is critical for interpreting the model’s behavior. Everything in this project is anchored on the synthetic CSV produced by `generator/generate_cyber_incidents.py`.

---

## Dataset overview

- **Path**: `data/cyber_incidents_simulated.csv`
- **Default volume**: 100,000 incidents spanning the 2024 calendar year
- **Classes**: `phishing`, `malware`, `access_abuse`, `data_exfiltration`, `policy_violation`, `web_attack`, `benign_activity`
- **Artifacts**: All notebooks, the CLI, and the baseline model load from this CSV, so keep it in sync with any custom changes.

### Schema cheat sheet

| Column                                             | Description                                                              |
| -------------------------------------------------- | ------------------------------------------------------------------------ |
| `event_id`                                         | Sequential identifier generated at write time                            |
| `timestamp`                                        | Randomized datetime between 2024-01-01 and 2024-12-31                    |
| `log_source`                                       | Source system (email gateway, EDR, proxy, firewall, DLP, etc.)           |
| `event_type`                                       | One of the seven incident classes, optionally flipped for noise          |
| `severity`                                         | `info`–`critical`, biased per event type (e.g., ransomware skews higher) |
| `mitre_technique`                                  | Representative ATT&CK technique(s) for that event                        |
| `user`, `device`                                   | Named accounts and hosts targeted in the scenario                        |
| `src_ip`, `dest_ip`, `src_country`, `dest_country` | Network attribution fields                                               |
| `src_port`, `dest_port`, `protocol`                | Transport context tuned to the event type                                |
| `detection_rule`                                   | Label for the analytic or alert that fired                               |
| `is_true_positive`                                 | Simple flag indicating whether the scenario is a true incident           |
| `description`                                      | Full narrative with noise, typos, and abbreviated tokens                 |
| `description_short`                                | SOC-friendly summary                                                     |
| `description_user_report`                          | “How a user might describe it” phrasing                                  |
| `short_log`                                        | WAF/SIEM style single-line log for quick scanning                        |

Use the rich text fields (`description`, `description_short`, `description_user_report`, `short_log`) interchangeably across notebooks to test robustness against slightly different perspectives.

---

## Realism features baked into the generator

The `generate_cyber_incidents.py` script introduces several mechanisms to avoid a too-perfect dataset:

- **Confusable classes**: Sets such as `web_attack` vs `access_abuse` vs `benign_activity` share vocabulary on purpose.
- **Label noise**: `LABEL_NOISE_RATE` and `NEIGHBOR_LABELS` flip about 8 % of labels to neighboring classes.
- **Severity and MITRE biasing**: Helper functions select severities, MITRE techniques, and log sources that match the event type.
- **Narrative noise**: Spelling swaps, abbreviations, and templated verbs keep `description` slightly messy while `description_short` stays concise.
- **True/false positive signal**: `is_true_positive` is biased toward `malware`, `data_exfiltration`, etc., so analysts can explore downstream filtering rules.

These touches make downstream evaluation (confusion matrices, scenario notebooks, CLI uncertainty logic) feel closer to a real SOC dataset.

---

## Regenerating or customizing the dataset

1. **Regenerate with defaults** (100k rows to the same CSV):

   ```bash
   python generator/generate_cyber_incidents.py
   ```

2. **Customize volume or output path** by calling `generate_events` directly:

   ```bash
   python - <<'PY'
   from generator.generate_cyber_incidents import generate_events
   generate_events(n_events=25000, outfile="data/cyber_incidents_small.csv")
   PY
   ```

3. **Tweak behavior** inside `generator/generate_cyber_incidents.py`:

   - Adjust `EVENT_TYPES` to add/remove classes.
   - Change `LABEL_NOISE_RATE`/`NEIGHBOR_LABELS` for more or less confusion.
   - Extend vocab lists (`DETECTION_RULES`, `MALWARE_SUBTYPES`, etc.) to add new textures.

Re-run any affected notebooks or retrain models after regenerating so artifacts remain consistent with the CSV on disk. The `tests/test_model_artifacts.py` suite will fail fast if the expected files or class labels go missing.

---

## Production Generation Scripts

For large-scale dataset generation (100K+ events) with LLM enhancement, checkpointing, and monitoring, the project includes professional bash orchestration scripts:

### Quick Start

```bash
# Launch 100K event generation (default)
cd generator
./launch_generator.sh

# Monitor in real-time
./monitor_generation.sh --watch
```

### Scripts Overview

| Script                      | Purpose                                                                               |
| --------------------------- | ------------------------------------------------------------------------------------- |
| **`launch_generator.sh`**   | Production launcher with LLM integration, checkpointing, background execution         |
| **`monitor_generation.sh`** | Real-time monitoring dashboard with GPU metrics, throughput analysis, ETA calculation |

### Key Features

**launch_generator.sh**:

- **LLM Enhancement**: Optional Llama-2-13B-Chat integration for realistic narrative rewrites (1% of events by default)
- **Checkpoint/Resume**: Automatic progress saving every 100 events - resume interrupted generations seamlessly
- **Background Processing**: Uses `nohup` for SSH-safe, unattended operation
- **Interactive Resume**: Prompts when existing files detected (resume vs fresh start)
- **Environment Configuration**: Automatically sets LLM model paths, rewrite probability, temperature

**monitor_generation.sh**:

- **Process Metrics**: Real-time CPU/memory usage, runtime, efficiency (events/CPU%, events/GB)
- **Progress Tracking**: Visual progress bar, percentage complete, ETA with full timestamp
- **GPU Acceleration** (Apple Silicon): Metal GPU detection, LLM model info, inference speed (~18.5 tokens/sec)
- **Throughput Analysis**: Events/second average, trend detection (accelerating/declining/steady)
- **Performance Dashboard**: Chunk timing, last 5 log entries, file sizes, quick action commands
- **Watch Mode**: Auto-refresh every N seconds (default 30s)
- **Simple Mode**: ASCII symbols for problematic terminals (`--simple` or `--simple-color`)

### Usage Examples

```bash
# Generate 50K events with custom name
./launch_generator.sh 50000 training_data

# Fresh start (delete existing files)
./launch_generator.sh 100000 cyber_incidents_simulated --fresh

# Monitor with auto-refresh every 10 seconds
./monitor_generation.sh --watch 10

# Monitor custom dataset in simple mode
./monitor_generation.sh my_dataset --simple-color --watch
```

### LLM Configuration (in launch_generator.sh)

```bash
export NLP_TRIAGE_LLM_GENERATOR=1             # Enable LLM generation
export NLP_TRIAGE_LLM_REWRITE_PROB=0.01       # 1% rewrite rate (balanced quality/speed)
export NLP_TRIAGE_LLM_TEMPERATURE=0.2         # Focused, deterministic output
export NLP_TRIAGE_LLM_MAX_RETRIES=3           # Retry failed LLM calls
export NLP_TRIAGE_LLM_BACKEND="models/llama-2-13b-chat.Q5_K_S.gguf"
```

**Performance**:

- **With LLM (1% rewrite)**: ~3-5 events/sec (100K events in 6-9 hours)
- **Without LLM**: ~50-100 events/sec (100K events in 20-30 minutes)

### Output Files

All outputs written to `data/` directory:

| File                             | Description                                                             |
| -------------------------------- | ----------------------------------------------------------------------- |
| `{dataset_name}.csv`             | Main dataset (100K rows ~99MB uncompressed)                             |
| `{dataset_name}.log`             | Detailed generation log with timestamps                                 |
| `{dataset_name}_checkpoint.json` | Progress state for resume capability                                    |
| `{dataset_name}_llm_report.json` | LLM usage statistics (rewrites attempted/applied, success rate, timing) |
| `nohup_output.log`               | Raw stdout/stderr from background process                               |

### Checkpointing System

Progress saved every 100 events:

```json
{
  "last_completed_event": 25000,
  "total_events": 100000,
  "chunks_written": 250,
  "timestamp": "2024-11-22T10:30:15",
  "status": "running"
}
```

**Resume behavior**: Generator reads checkpoint, continues from `last_completed_event + 1`, appends to CSV without re-writing header.

### Monitoring Dashboard Sample

```
🛠️  CYBERSECURITY DATASET GENERATION MONITOR
Dataset: cyber_incidents_simulated
Started: Fri Nov 22 08:15:30 CST 2024
ETA: Fri Nov 22 14:32:15 CST 2024

📈  PROCESS STATUS
✅  Generation process RUNNING (PID: 12345)
   CPU Usage: 125.3% (7.8% per core, 16 cores)
   Memory Usage: 8.2% (2.1GB / 32.0GB)
   🎮 GPU: Metal (Apple M2 Max - 38 cores)
      LLM Model: llama-2-13b-chat.Q5_K_S.gguf
      Enhancement: 0.8% of events (99.4% success)
      GPU Throughput: 375.2/hr (9.6s avg per rewrite)
   Efficiency: 1,234 events/CPU%, 15,600 events/GB

📈  PROGRESS STATUS
🚀 25000/100000 (25.0%)
   [████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 25.0%
   📈 Throughput: Steady

⚡ PERFORMANCE
   Generation runtime: 2h 15m 42s
   Time per event: 0.3s
   Events/second: 3.088
   Estimated time remaining: 6h 15m
```

### Process Management

```bash
# Check if generation is running
pgrep -f "generate_cyber_incidents.py"

# Kill running generation
pkill -f generate_cyber_incidents

# View real-time logs
tail -f data/cyber_incidents_simulated.log

# Inspect checkpoint
cat data/cyber_incidents_simulated_checkpoint.json | jq
```

### Customization

**Environment variables** (set before launching):

```bash
# Higher LLM rewrite rate (10% of events)
export NLP_TRIAGE_LLM_REWRITE_PROB=0.10

# More creative LLM output
export NLP_TRIAGE_LLM_TEMPERATURE=0.7

# Verbose LLM debugging
export NLP_TRIAGE_LLM_DEBUG=1

# Custom model path
export NLP_TRIAGE_LLM_BACKEND="/path/to/custom-model.gguf"
```

**Direct Python call** (manual control):

```bash
cd generator
python generate_cyber_incidents.py \
  --n-events 50000 \
  --outfile ../data/my_dataset.csv \
  --start-date 2024-01-01 \
  --end-date 2024-12-31 \
  --chunk-size 100 \
  --use-llm \
  --rewrite-report ../data/my_dataset_llm_report.json
```

### Troubleshooting

**Slow generation**: Lower `NLP_TRIAGE_LLM_REWRITE_PROB` (default 0.01 = 1%) or disable LLM entirely by commenting out `export NLP_TRIAGE_LLM_GENERATOR=1` in `launch_generator.sh`.

**Resume not working**: Check checkpoint file exists (`ls -lh data/{dataset}_checkpoint.json`) and wasn't deleted. Ensure dataset name matches.

**Monitor shows "No active generation"**: Specify dataset name explicitly: `./monitor_generation.sh my_custom_dataset --watch`

**LLM model not found**: Download Llama-2-13B-Chat GGUF (Q5_K_S quantization, ~7.5GB) to `models/` directory, or disable LLM in launcher script.

### Complete Documentation

For comprehensive usage, GPU metrics, performance optimization, example workflows, and advanced configurations, see [Production Generation Guide](production-generation.md).
