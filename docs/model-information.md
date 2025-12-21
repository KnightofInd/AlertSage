

# Model Information

## 📄 Model Card — NLP Incident Triage (v0.2.0)

**Model Name:** NLP Incident Triage  
**Version:** 0.2.0  
**Author:** Chris Campbell (@texasbe2trill)  
**Intended Use:** Educational and research-grade NLP classifier trained on synthetic cybersecurity incident narratives. Designed to demonstrate SOC triage automation concepts—not to replace production security tooling.

---

## 1. Model Description
A TF–IDF + Logistic Regression classifier that assigns cybersecurity incident narratives to high-level event types:

```
phishing  
malware  
access_abuse  
data_exfiltration  
policy_violation  
web_attack  
benign_activity
```

The model uses:
- Synthetic SOC-style data with narrative templates  
- MITRE ATT&CK–inspired phrasing  
- Noise injection + label flipping for realism  
- Uncertainty-aware predictions (`uncertain` fallback)  
- Difficulty modes (`soc-medium`, `soc-hard`)  

---

## 2. Intended Use
The model is suitable for:

- Demonstrating NLP-based SOC triage workflows  
- Academic or training environments  
- Research on text classification methods  
- Early-stage prototyping of incident summarization/triage tools  

---

## 3. Not Intended For
**Not for production SOC or IR operations.**  
**Not designed for automated high-stakes decisions.**  
**Not trained on real security logs.**

---

## 4. Training Data
- 100% synthetic dataset  
- Multiple event types with realistic SOC-style variation  
- Includes ambiguous scenarios and misdirection  
- MITRE-inspired narrative segments (Technique IDs included as text)  
- No PII, customer data, or proprietary logs  

---

## 5. Evaluation
Evaluated using:

- Synthetic hold‑out test set  
- 18‑scenario SOC test suite  
- Ambiguity stress tests  
- Model comparison across LogReg, Linear SVM, RandomForest  
- Probability calibration analysis  

Observed behavior:

- ~92% accuracy on synthetic test set  
- Strong performance on clear-cut phishing/malware/exfiltration  
- Realistic degradation on ambiguous or noisy cases  
- Uncertainty thresholding improves stability  

---

## 6. Ethical Considerations
- Only synthetic data used  
- No real-world adversary emulation  
- User should maintain human-in-the-loop validation  
- MITRE ATT&CK® used with required attribution:
  - “MITRE ATT&CK® is a registered trademark of The MITRE Corporation.”

---

## 7. Limitations
- Not trained on real logs or telemetry  
- Cannot detect rare SOC events outside template patterns  
- Limited ability to reason over long multi-sentence reports  
- Vocabulary tied to generator styles  

---

## 8. Recommendations for Future Work
- Expand training set with richer MITRE-derived semantics  
- Add vendor-specific log styles (MDE, CrowdStrike, Okta, etc.)  
- Introduce structured indicators (IPs, ports, geodata) as model features  
- Explore transformer-based encoders for long-text handling  
- Increase scenario test suite to 50+ cases  

---

## 9. Version History
### v0.2.0
- MITRE-inspired narrative enrichment  
- Difficulty modes (`soc-medium`, `soc-hard`)  
- Bulk analysis mode  
- SOC summary output  
- Improved CLI formatting and progress bar  
- Updated documentation and model card  

---

If you would like, I can also generate a printable PDF version of this model card for inclusion in releases.