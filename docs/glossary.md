# Glossary

## Terms

### Checkpoint

Persistent state file enabling resumable dataset generation. Contains progress, timestamps, and metadata.

### Confidence Threshold

Minimum probability score required for a label. Below threshold triggers "uncertain" fallback.

### Difficulty Mode

Setting controlling strictness of uncertainty handling:

- **default**: Standard thresholds
- **soc-medium**: Moderate strictness
- **soc-hard**: Maximum strictness for edge cases

### GGUF

GPT-Generated Unified Format. File format for quantized LLM models used by llama.cpp.

### Guardrails

Safety mechanisms preventing LLM hallucinations:

- JSON parsing validation
- SOC keyword intelligence
- Label normalization
- Timeout protection

### Incident

Security event requiring investigation. Represented as natural language narrative in this system.

### LLM

Large Language Model. Used for dataset enhancement and second-opinion triage.

### MITRE ATT&CK®

Knowledge base of adversary tactics and techniques. Used for incident enrichment and mapping.

### Quantization

Model compression technique reducing size/memory at slight accuracy cost (Q4, Q5, Q8).

### Rewrite Engine

LLM-powered component enhancing synthetic narratives during generation.

### Second Opinion

LLM-assisted classification for uncertain cases. Provides alternative perspective with rationale.

### SOC

Security Operations Center. Team responsible for monitoring and responding to security incidents.

### Synthetic Data

Artificially generated training data. This project uses 100% synthetic incidents.

### TF-IDF

Term Frequency-Inverse Document Frequency. Statistical measure for text feature extraction.

### Triage

Process of categorizing and prioritizing incidents based on severity and type.

### Uncertain

Label assigned when classifier confidence is below threshold. Indicates manual review needed.

### Vectorization

Conversion of text to numerical representations for ML processing.

## Acronyms

| Acronym | Full Term                                                      |
| ------- | -------------------------------------------------------------- |
| API     | Application Programming Interface                              |
| ATT&CK  | Adversarial Tactics, Techniques & Common Knowledge             |
| CI/CD   | Continuous Integration/Continuous Deployment                   |
| CLI     | Command-Line Interface                                         |
| CPU     | Central Processing Unit                                        |
| CSV     | Comma-Separated Values                                         |
| EDR     | Endpoint Detection and Response                                |
| ETA     | Estimated Time of Arrival                                      |
| GGUF    | GPT-Generated Unified Format                                   |
| GPU     | Graphics Processing Unit                                       |
| IR      | Incident Response                                              |
| JSON    | JavaScript Object Notation                                     |
| JSONL   | JSON Lines (one JSON object per line)                          |
| LLM     | Large Language Model                                           |
| MITRE   | Massachusetts Institute of Technology Research and Engineering |
| ML      | Machine Learning                                               |
| NLP     | Natural Language Processing                                    |
| RAM     | Random Access Memory                                           |
| SIEM    | Security Information and Event Management                      |
| SOAR    | Security Orchestration, Automation and Response                |
| SOC     | Security Operations Center                                     |
| TF-IDF  | Term Frequency-Inverse Document Frequency                      |
| UI      | User Interface                                                 |
| URL     | Uniform Resource Locator                                       |

## File Extensions

| Extension | Description                                    |
| --------- | ---------------------------------------------- |
| `.csv`    | Comma-separated values dataset file            |
| `.joblib` | Serialized scikit-learn model or vectorizer    |
| `.json`   | JSON configuration or results file             |
| `.jsonl`  | JSON Lines (bulk results, one record per line) |
| `.log`    | Text log file                                  |
| `.md`     | Markdown documentation file                    |
| `.gguf`   | Quantized LLM model file                       |
| `.py`     | Python source code file                        |
| `.sh`     | Shell script file                              |
| `.yml`    | YAML configuration file                        |

---

For technical terms, see [Architecture](architecture.md) and [Model Information](model-information.md).
