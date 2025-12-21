# Production Dataset Generation

This guide covers production-scale dataset generation using LLM-enhanced scripts for creating realistic, large-scale cybersecurity incident datasets.

---

## Overview

The production generation system consists of two key bash scripts that orchestrate the Python generator with advanced features:

1. **`launch_generator.sh`** - Launches dataset generation with checkpointing, LLM integration, and background processing
2. **`monitor_generation.sh`** - Real-time monitoring dashboard with GPU metrics, throughput analysis, and performance tracking

These scripts are designed for **long-running, unattended dataset generation** (hours to days) with automatic resume capability.

---

## Quick Start

### Basic Generation (100K events, default settings)

```bash
cd generator
./launch_generator.sh
```

### Custom Dataset Size and Name

```bash
# Generate 50,000 events with custom name
./launch_generator.sh 50000 my_custom_dataset

# Fresh start (delete existing files)
./launch_generator.sh 100000 cyber_incidents_simulated --fresh
```

### Monitor Progress

```bash
# Single snapshot
./monitor_generation.sh

# Auto-refresh every 30 seconds
./monitor_generation.sh --watch

# Auto-refresh every 10 seconds
./monitor_generation.sh --watch 10

# Monitor custom dataset
./monitor_generation.sh my_custom_dataset --watch
```

---

## launch_generator.sh

### Purpose

Launches the Python dataset generator as a background process with:

- **LLM-enhanced generation**: Optional Llama-2-13B-Chat for realistic narrative rewrites
- **Checkpoint/resume**: Automatic progress saving and resume capability
- **Background processing**: Runs via `nohup` for SSH-safe operation
- **Error recovery**: Handles interruptions gracefully

### Usage

```bash
./launch_generator.sh [events] [dataset_name] [--fresh]
```

### Parameters

| Parameter      | Description                               | Default                   |
| -------------- | ----------------------------------------- | ------------------------- |
| `events`       | Number of incidents to generate           | 100000                    |
| `dataset_name` | Output dataset name (no `.csv` extension) | cyber_incidents_simulated |
| `--fresh`      | Delete existing files and start fresh     | Resume from checkpoint    |

### Examples

```bash
# Default: 100K events, resume from checkpoint
./launch_generator.sh

# 50K events with custom name
./launch_generator.sh 50000 training_data

# 200K events, fresh start (delete old files)
./launch_generator.sh 200000 large_dataset --fresh

# Resume existing generation
./launch_generator.sh 100000 cyber_incidents_simulated
```

### LLM Configuration

The script automatically configures the LLM with production-optimized settings:

```bash
export NLP_TRIAGE_LLM_GENERATOR=1             # Enable LLM generation
export NLP_TRIAGE_LLM_REWRITE_PROB=0.01       # 1% of events get LLM enhancement
export NLP_TRIAGE_LLM_TEMPERATURE=0.2         # Focused, deterministic output
export NLP_TRIAGE_LLM_MAX_RETRIES=3           # Retry failed LLM calls
export NLP_TRIAGE_LLM_DEBUG=0                 # Disable verbose logging
export NLP_TRIAGE_LLM_BACKEND="models/llama-2-13b-chat.Q5_K_S.gguf"
```

**Model**: Llama-2-13B-Chat (7.5GB GGUF quantized)

- Requires: ~10GB RAM (M1/M2 Mac with Metal acceleration)
- Performance: ~10-20 tokens/sec on Apple Silicon

### Output Files

| File                                  | Description                               |
| ------------------------------------- | ----------------------------------------- |
| `data/{dataset_name}.csv`             | Main dataset (100K rows ~99MB)            |
| `data/{dataset_name}.log`             | Detailed generation log with timestamps   |
| `data/{dataset_name}_checkpoint.json` | Progress state for resume capability      |
| `data/{dataset_name}_llm_report.json` | LLM usage statistics and metrics          |
| `data/nohup_output.log`               | Raw stdout/stderr from background process |

### Interactive Resume Handling

If existing files are detected without `--fresh`, you'll be prompted:

```
⚠️  WARNING: Existing files detected:
   - data/cyber_incidents_simulated.csv
   - data/cyber_incidents_simulated_checkpoint.json

Choose an option:
   r) Resume from checkpoint (default)
   f) Fresh start (delete existing files)
   q) Quit
Choice (r/f/q):
```

### Process Management

```bash
# Check if generation is running
pgrep -f "generate_cyber_incidents.py"

# Kill running generation
pkill -f generate_cyber_incidents

# View background output
tail -f data/nohup_output.log

# View detailed logs
tail -f data/cyber_incidents_simulated.log
```

---

## monitor_generation.sh

### Purpose

Real-time monitoring dashboard providing:

- **Process status**: CPU, memory, runtime metrics
- **Progress tracking**: Events completed, ETA, throughput
- **GPU acceleration**: Metal/Apple Silicon metrics when using LLM
- **Performance analysis**: Throughput trends, efficiency metrics
- **File status**: Dataset size, log sizes

### Usage

```bash
./monitor_generation.sh [dataset_name] [options]
```

### Options

| Option                     | Description                                                     |
| -------------------------- | --------------------------------------------------------------- |
| `dataset_name`             | Name of dataset to monitor (default: cyber_incidents_simulated) |
| `--watch`, `-w [interval]` | Auto-refresh mode (default 30s interval)                        |
| `--simple`, `-s`           | ASCII symbols, no colors (for problematic terminals)            |
| `--simple-color`           | ASCII symbols WITH colors (best for SSH/tmux)                   |
| `--help`, `-h`             | Show help message                                               |

### Examples

```bash
# Single snapshot
./monitor_generation.sh

# Auto-refresh every 30 seconds
./monitor_generation.sh --watch

# Auto-refresh every 10 seconds
./monitor_generation.sh --watch 10

# Monitor custom dataset
./monitor_generation.sh my_dataset --watch

# Simple mode for SSH/tmux
./monitor_generation.sh --simple-color --watch
```

### Dashboard Sections

#### 1. Process Status

- **PID**: Background process identifier
- **CPU Usage**: Per-core and total CPU utilization
- **Memory Usage**: Process memory consumption vs total system RAM
- **Runtime**: Process uptime
- **GPU Acceleration** (Apple Silicon only):
  - Metal GPU detection and core count
  - LLM model information (Llama-2-13B-Chat)
  - GPU throughput metrics (rewrites/hr, tokens/sec)
  - Enhancement rate (% of events LLM-enhanced)

#### 2. Progress Status

- **Real-time progress**: Current/Total events with percentage
- **Progress bar**: Visual 50-character bar with completion indicator
- **Generation status**: Generating/Initializing/LLM loading
- **Throughput trend**: Accelerating/Declining/Steady analysis
- **ETA**: Estimated completion time with full timestamp

#### 3. File Status

- **Dataset file**: Size in human-readable format (MB/GB) with event count
- **Log file**: Generation log size
- **Nohup output**: Background process output size

#### 4. Recent Activity

- **Last 5 log entries**: Tail of detailed log
- **Chunk analysis**:
  - Average chunk interval (time between chunks)
  - Last chunk interval (most recent timing)
  - Total chunks completed

#### 5. Performance Metrics

- **Generation runtime**: Total time since start
- **Time per event**: Average seconds per incident
- **Events/second**: Throughput rate
- **Progress velocity**: Percentage completion per hour
- **Estimated time remaining**: Hours/minutes until completion
- **Resource efficiency**: Events per CPU%, Events per GB RAM

### Sample Output

```
🛠️  CYBERSECURITY DATASET GENERATION MONITOR
==============================================
Dataset: cyber_incidents_simulated
Started: Fri Nov 22 08:15:30 CST 2024
ETA: Fri Nov 22 14:32:15 CST 2024

📈  PROCESS STATUS
-----------------
✅  Generation process RUNNING (PID: 12345)
   CPU Usage: 125.3% (7.8% per core, 16 cores total)
   Memory Usage: 8.2% (2.1GB of 32.0GB total)
   Runtime: 2:15:42 (process uptime)
   🎮 GPU Acceleration: Metal (Apple M2 Max - 38 cores)
      LLM Model: llama-2-13b-chat.Q5_K_S.gguf
      LLM Activity: 845/850 rewrites processed
      Enhancement: 0.8% of events (99.4% success rate)
      GPU Throughput: 375.2/hr (9.6s avg per rewrite)
      Inference Speed: ~18.5 tokens/sec
   Efficiency: 1,234 events/CPU%, 15,600 events/GB

📈  PROGRESS STATUS
------------------
🚀 Generation active: 25000/100000 (25.0%)
   [████████████░░░░░░░░░░░░░░░░░░░░░░░░░░░░] 25.0% Complete
   Status: Generating events...
   📈 Throughput: Steady

📁  FILE STATUS
--------------
✅ Dataset: 24.5M (25000 events)
✅ Log file: 1.2M
✅ Nohup output: 45K

📝  RECENT ACTIVITY
------------------
Last 5 log entries:
   2024-11-22 10:30:15 - Writing chunk 250
   2024-11-22 10:30:12 - Generating events: 25000/100000
   2024-11-22 10:29:58 - Writing chunk 249
   ...

📦 Chunk Analysis:
   Average chunk interval: 5m 23s
   Last chunk interval: 5m 15s
   Total chunks completed: 250

⚡ PERFORMANCE
-------------
   Generation runtime: 2h 15m 42s
   Started: 2024-11-22 08:15:30
   Progress velocity: 11.1%/hour
   Time per event: 0.3s
   Estimated time remaining: 6h 15m
   Events/second: 3.088 (avg)

🛠️  QUICK ACTIONS
----------------
Monitor real-time: tail -f ../data/cyber_incidents_simulated.log
Check progress:    cat ../data/cyber_incidents_simulated_checkpoint.json | jq
Kill process:      pkill -f generate_cyber_incidents
View nohup output: tail -f ../data/nohup_output.log

🚀 STATUS: Generation active (25.0% complete)
```

### GPU Metrics (Apple Silicon)

When LLM enhancement is enabled on Apple Silicon Macs, the monitor shows:

- **GPU Model**: e.g., "Apple M2 Max - 38 cores"
- **LLM Model**: Loaded model file (llama-2-13b-chat.Q5_K_S.gguf)
- **Enhancement Rate**: Percentage of events LLM-enhanced
- **GPU Throughput**: Rewrites per hour, average time per rewrite
- **Inference Speed**: Estimated tokens/second
- **Success Rate**: % of successful LLM rewrites

### Performance Trending

The monitor calculates throughput trends by sampling recent progress:

- **Accelerating**: Throughput increasing (shows +X%)
- **Steady**: Consistent throughput
- **Declining**: Throughput decreasing (shows -X%)

---

## Checkpointing System

### How It Works

The generator saves progress every **100 events** (configurable via `--chunk-size`):

```json
{
  "last_completed_event": 25000,
  "total_events": 100000,
  "chunks_written": 250,
  "timestamp": "2024-11-22T10:30:15",
  "status": "running",
  "generation_start_time": "2024-11-22T08:15:30"
}
```

### Resume Behavior

When you restart the generator:

1. Checks for existing checkpoint file
2. Reads `last_completed_event`
3. Continues from event **25001**
4. Appends to existing CSV file

**No data is duplicated or lost** - the CSV header is NOT re-written on resume.

### Manual Checkpoint Inspection

```bash
# View checkpoint status
cat data/cyber_incidents_simulated_checkpoint.json | jq

# Check progress percentage
jq -r '"\(.last_completed_event)/\(.total_events) = \((.last_completed_event / .total_events * 100) | tostring + "%")"' \
  data/cyber_incidents_simulated_checkpoint.json
```

---

## LLM-Enhanced Generation

### What Gets Enhanced?

With `NLP_TRIAGE_LLM_REWRITE_PROB=0.01` (default), approximately **1% of events** receive LLM enhancement:

- **Narrative rewriting**: More realistic phrasing and SOC language
- **Technical detail addition**: Specific IPs, file hashes, timestamps
- **Contextual enrichment**: Background information, user quotes
- **Complexity variation**: Mix of terse/verbose descriptions

### LLM Report

After generation, check `data/{dataset_name}_llm_report.json`:

```json
{
  "rewrites_attempted": 1050,
  "rewrites_applied": 1043,
  "rewrite_success_rate": 0.993,
  "average_rewrite_time_seconds": 9.6,
  "total_llm_time_seconds": 10012.8,
  "model_path": "models/llama-2-13b-chat.Q5_K_S.gguf",
  "temperature": 0.2,
  "max_retries": 3
}
```

**Metrics explanation**:

- **rewrites_attempted**: Total LLM calls triggered (1% of 100K = ~1000)
- **rewrites_applied**: Successfully enhanced events
- **success_rate**: Percentage of successful LLM rewrites (typically 99%+)
- **average_rewrite_time**: Seconds per LLM call (~10s for 13B model)
- **total_llm_time**: Cumulative GPU inference time

### Disabling LLM

For faster generation without LLM enhancement:

```bash
# Edit launch_generator.sh and comment out:
# export NLP_TRIAGE_LLM_GENERATOR=1

# Or manually run without LLM:
python generate_cyber_incidents.py --n-events 100000 --outfile ../data/dataset.csv
```

**Speed comparison**:

- **With LLM (1% rewrite)**: ~3-5 events/sec (~6-9 hours for 100K)
- **Without LLM**: ~50-100 events/sec (~20-30 minutes for 100K)

---

## Advanced Usage

### Custom Python Call (Manual Control)

```bash
cd generator

# Direct Python call with all parameters
python generate_cyber_incidents.py \
  --n-events 50000 \
  --outfile ../data/my_dataset.csv \
  --start-date 2024-01-01 \
  --end-date 2024-12-31 \
  --chunk-size 100 \
  --log-file ../data/my_dataset.log \
  --checkpoint-file ../data/my_dataset_checkpoint.json \
  --use-llm \
  --rewrite-report ../data/my_dataset_llm_report.json
```

### Environment Variable Customization

```bash
# Higher LLM rewrite rate (10% of events)
export NLP_TRIAGE_LLM_REWRITE_PROB=0.10

# More creative LLM output
export NLP_TRIAGE_LLM_TEMPERATURE=0.7

# Verbose LLM debugging
export NLP_TRIAGE_LLM_DEBUG=1

# Custom model path
export NLP_TRIAGE_LLM_BACKEND="/path/to/custom-model.gguf"

# Then launch
./launch_generator.sh
```

### Multiple Concurrent Generations

You can run multiple generators simultaneously with different dataset names:

```bash
# Terminal 1: Generate training dataset
./launch_generator.sh 100000 training_data --fresh

# Terminal 2: Generate validation dataset
./launch_generator.sh 20000 validation_data --fresh

# Terminal 3: Monitor both
./monitor_generation.sh training_data --watch &
./monitor_generation.sh validation_data --watch
```

**Note**: Each generator will compete for CPU/GPU resources. On Apple Silicon, running 2 LLM-enhanced generators will slow both down ~50%.

---

## Troubleshooting

### Generator Won't Start

**Error**: `Generation already running (PID: 12345)`

**Solution**:

```bash
# Kill existing process
pkill -f generate_cyber_incidents

# Or use --fresh to auto-kill
./launch_generator.sh 100000 my_dataset --fresh
```

### LLM Model Not Found

**Error**: `LLM model not found: models/llama-2-13b-chat.Q5_K_S.gguf`

**Solution**:

```bash
# Download the model (7.5GB)
cd models
# Use your preferred download method for Llama-2-13B-Chat GGUF Q5_K_S quantization

# Or disable LLM in launch_generator.sh
# Comment out: export NLP_TRIAGE_LLM_GENERATOR=1
```

### Slow Generation Speed

**Issue**: Only 0.5 events/sec with LLM enabled

**Causes**:

1. **High rewrite probability**: Check `NLP_TRIAGE_LLM_REWRITE_PROB` (should be 0.01-0.05)
2. **Large model**: 13B model is slower than 7B (but higher quality)
3. **Memory swapping**: System RAM exhausted, using swap
4. **Other processes**: GPU/CPU contention

**Solutions**:

```bash
# Lower rewrite probability
export NLP_TRIAGE_LLM_REWRITE_PROB=0.01  # 1% instead of 10%

# Use smaller 7B model (faster, lower quality)
export NLP_TRIAGE_LLM_BACKEND="models/llama-2-7b-chat.Q5_K_S.gguf"

# Disable LLM entirely
# Comment out: export NLP_TRIAGE_LLM_GENERATOR=1

# Close other applications to free RAM/GPU
```

### Monitor Shows "No active generation"

**Issue**: Process is running but monitor doesn't detect it

**Cause**: Process name mismatch (using custom dataset name)

**Solution**:

```bash
# Specify dataset name explicitly
./monitor_generation.sh my_custom_dataset --watch
```

### Resume Not Working

**Issue**: Generator starts from 0 instead of resuming

**Causes**:

1. Checkpoint file corrupted
2. Used `--fresh` flag
3. Dataset name mismatch

**Solution**:

```bash
# Check checkpoint exists
ls -lh data/cyber_incidents_simulated_checkpoint.json

# View checkpoint contents
cat data/cyber_incidents_simulated_checkpoint.json | jq

# If corrupted, delete and start fresh
rm data/cyber_incidents_simulated_checkpoint.json
./launch_generator.sh 100000 cyber_incidents_simulated --fresh
```

---

## Performance Optimization

### Maximizing Speed (No LLM)

```bash
# Disable LLM in launch_generator.sh
# Comment out: export NLP_TRIAGE_LLM_GENERATOR=1

# Larger chunk size (fewer disk writes)
# Edit generate_cyber_incidents.py: --chunk-size 1000

# Expected: ~50-100 events/sec (100K events in 20-30 minutes)
```

### Balancing Quality vs Speed

| Configuration | Speed        | Quality   | Time for 100K |
| ------------- | ------------ | --------- | ------------- |
| No LLM        | 50-100 evt/s | Good      | 20-30 min     |
| LLM 1%        | 3-5 evt/s    | Excellent | 6-9 hours     |
| LLM 5%        | 2-3 evt/s    | Best      | 10-15 hours   |
| LLM 10%       | 1-2 evt/s    | Overkill  | 15-24 hours   |

**Recommendation**: Use **1-2% LLM enhancement** for production datasets - provides excellent quality without excessive generation time.

### Resource Requirements

**Minimum**:

- 8GB RAM
- 2-core CPU
- 5GB disk space (for 100K events)

**Recommended** (with LLM):

- 16GB RAM (10GB for model + 6GB for system)
- 4+ core CPU (Apple Silicon M1/M2 ideal)
- 10GB disk space (dataset + logs + checkpoints)
- macOS with Metal support (for GPU acceleration)

**Optimal** (large-scale generation):

- 32GB+ RAM
- 8+ core CPU
- 50GB+ disk space (multiple datasets)
- Apple Silicon M1 Max/M2 Max/M3 (faster GPU)

---

## Example Workflows

### Quick Test Dataset (1K events, no LLM)

```bash
# Edit launch_generator.sh: comment out LLM_GENERATOR
./launch_generator.sh 1000 test_data --fresh
# Wait ~20-30 seconds
./monitor_generation.sh test_data
```

### Production Dataset (100K events, 1% LLM)

```bash
# Default configuration (already set in launch_generator.sh)
./launch_generator.sh 100000 cyber_incidents_simulated --fresh

# Monitor in another terminal
./monitor_generation.sh --watch 60  # Refresh every minute

# Expected completion: 6-9 hours
# Check completion: grep "completed successfully" data/cyber_incidents_simulated.log
```

### Large-Scale Dataset (500K events, overnight)

```bash
# Launch before leaving for the day
./launch_generator.sh 500000 large_dataset --fresh

# Monitor remotely via SSH (use simple mode)
ssh your-machine
cd /path/to/generator
./monitor_generation.sh large_dataset --simple-color --watch

# Expected completion: 30-45 hours with 1% LLM
```

---

## Best Practices

1. **Always use `--watch` mode** when monitoring long-running generations
2. **Check disk space** before large generations (`df -h`)
3. **Use checkpoints** - never start fresh unless necessary
4. **Review LLM report** after completion to validate enhancement success rate
5. **Test with small datasets** before committing to 100K+ event generations
6. **Monitor GPU temperature** on long runs (use Activity Monitor on macOS)
7. **Use `nohup`/background execution** for SSH sessions
8. **Keep rewrite probability low** (1-2%) for good quality without excessive time
9. **Archive completed datasets** with LLM reports for reproducibility
10. **Document your generation settings** in dataset metadata files

---

## Next Steps

After generating your dataset:

1. **Validate dataset quality**: Check `notebooks/01_explore_dataset.ipynb`
2. **Train models**: Follow notebooks 02-03 for feature engineering and baseline model
3. **Customize generator**: See `data-and-generator.md` for vocabulary/template modifications
4. **Share your dataset**: Consider contributing anonymized versions back to the project

For dataset structure and customization details, see [Data & Generator Guide](data-and-generator.md).
