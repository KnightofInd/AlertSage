

# 🚀 NLP-Driven Incident Triage — v0.2.0 Release Notes

This release delivers a major leap forward in realism, robustness, and usability.  
With enriched MITRE ATT&CK® narratives, an upgraded CLI, batch processing, improved documentation, and enhanced testing, the project now behaves much closer to a lightweight NLP SOC analyst assistant.

---

## 🔥 Major Enhancements

### 🧠 MITRE ATT&CK® Narrative Enrichment
- Incident generator now embeds realistic MITRE techniques across all event types:
  - Phishing → T1566 (various subtypes)
  - Malware → T1486, T1059 (PowerShell), etc.
  - Access Abuse → T1078, T1110
  - Web Attack → T1190, T1110
  - Policy Violations → mapped where relevant
- Added `mitre_clause` generation per event.
- Documentation updated with required MITRE license attribution.

---

## 💻 CLI Upgrades

### ✨ Rich UI & Banner
- New ASCII NLPTriage banner on start.
- Colorized output, aligned columns, and better readability.
- Uses `rich` for tables, highlighting, and labeling.

### 🤖 Difficulty Modes (Uncertainty Handling)
New flag:
```
--difficulty {default, soc-medium, soc-hard}
```
- Adjusts the strictness for marking predictions as `uncertain`.
- `soc-hard` simulates cautious SOC analyst behavior.

### 📂 Bulk Mode (New!)
New flags:
```
--input-file incidents.txt
--output-file results.jsonl
```
- Supports batch-classifying hundreds of incidents.
- Writes results as JSONL.
- Includes an **automated summary**:
  - event-type distribution
  - uncertainty rate
  - MITRE technique counts (from generator)
  - suggested analyst review priorities

### 🎯 Prediction Enhancements
- Cleaner uncertainty threshold logic.
- Better sorting of probabilities.
- Improved preprocessing alignment between training and inference.

---

## 🧱 Data & Modeling Improvements
- More realistic SOC narratives with ATT&CK technique references.
- Expanded variation across event types.
- Added ambiguous real-world-like descriptions for robustness.
- Updated dataset to align with generator improvements.

---

## 📘 Documentation & Website (MkDocs)
- All docs updated to reflect new CLI, features, and MITRE attribution.
- New or updated pages:
  - CLI Usage
  - Modeling & Evaluation
  - Getting Started
  - Limitations + MITRE License
  - Realistic Model Behavior

---

## 🧪 Tests & CI
- Expanded pytest suite:
  - prediction structure tests
  - artifact loading tests
  - uncertainty logic tests
  - CLI helper tests
- Fixed issues with test imports and artifact loading.
- GitHub CI workflow updated to validate on PRs.

---

## 📦 Packaging & Structure
- Project supports:
  - `pip install -e .`
  - `nlp-triage` console entry point
- Improved `pyproject.toml`, `README.md`, and MkDocs structure.

---

## 🛠️ Bug Fixes
- Fixed issues related to path imports in CLI.
- Resolved LFS model load errors.
- Fixed probability length assumptions in tests.
- Corrected documentation sync issues.

---

## 🏁 Summary
**v0.2.0** transforms the project from a baseline demo into a far more realistic SOC triage assistant.  
With MITRE integration, batch mode, enhanced CLI, and polished documentation, the project is now ready for broader use, portfolio presentation, and future extensions.

---

## 🏷️ Upgrade Instructions
To install or upgrade locally:

```bash
pip install -e .
```

If you're using editable mode and updated the CLI, reinstall:

```bash
pip install -e . --force-reinstall
```

---

## 📎 MITRE ATT&CK® Notice
This project includes derived technique names and references from the  
MITRE ATT&CK® framework.  
ATT&CK® is licensed under CC BY-NC-SA 4.0.  
See: https://attack.mitre.org/resources/terms-of-use/