# Limitations & Safety

!!! warning "Educational / research-grade only"
    This project is intended for **learning, experimentation, and portfolio use**.  
    It is **not** designed or validated as production incident response tooling.

## Key Limitations

- **Synthetic-only training**  
  The model is trained entirely on synthetic incidents. While carefully designed, they do not fully capture the variability, noise, and corner cases of real SOC tickets and alerts.

- **Misclassification of edge cases**  
  Borderline or cleverly worded narratives may be misclassified. Some classes naturally overlap (e.g., `data_exfiltration` vs `policy_violation`, `web_attack` vs `benign_activity`).

- **Not for unsupervised live use**  
  The CLI is designed as a **decision-support aid** and educational demo, not as an unsupervised gatekeeper for real-world security decisions.

- **No real-time integration**  
  There is no direct integration with SIEM/EDR/SOAR platforms; any such integration would require additional engineering, monitoring, and governance.

---

## Recommended Usage

- Use as a **sandbox** for experimenting with:
  - Synthetic data generation
  - NLP modeling patterns
  - Evaluation frameworks and scenario-based testing
- Treat model outputs as **advisory hints**, not final ground truth.
- If you adapt this for real-world use, involve:
  - Security engineers and incident responders
  - MLOps and governance teams
  - Rigorous validation with real data and monitoring