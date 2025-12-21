# MITRE ATT&CK® Attribution

This project makes limited, research-focused use of the **MITRE ATT&CK®** knowledge base.

Specifically, the synthetic incident generator and modeling notebooks:

- Reference **ATT&CK technique IDs** (for example, `T1078`, `T1190`, `T1486`, `T1566`),
- Include **lightly paraphrased language** inspired by public ATT&CK technique descriptions,
- Use these techniques to make simulated adversary behavior more realistic in narrative text fields.

No proprietary or internal threat intel is used; all references are drawn from publicly available ATT&CK content and are intended for educational and portfolio purposes only.

## Trademarks and license

MITRE ATT&CK® and ATT&CK® are registered trademarks of **The MITRE Corporation**.

ATT&CK data is provided by The MITRE Corporation and is licensed under the
**Creative Commons Attribution-ShareAlike 4.0 International License (CC BY-SA 4.0)**.

For full details, see the official MITRE ATT&CK site and licensing information.

## How this project uses ATT&CK

Within this repository, ATT&CK references primarily appear in:

- The synthetic data generator (`generator/generate_cyber_incidents.py`), where certain
  narratives add clauses such as "This behavior aligns with MITRE ATT&CK technique T1486"
  to emulate analyst-style writeups.
- Modeling and evaluation notebooks, which occasionally refer to relevant tactics or
  techniques when discussing example incidents or patterns (for example, ransomware
  encryption mapped to `T1486`, phishing mapped to `T1566`, or web exploitation mapped
  to `T1190`).

These references are **contextual aids** to make the simulated incidents feel more
SOC-realistic and to help readers connect incident categories to canonical ATT&CK
techniques. They are **not** intended to be authoritative mappings and should not be
used as the sole basis for production detection logic.

## Scope and limitations

- The dataset is **synthetic** and only loosely aligned to ATTATT&CK many edge cases and
  real-world nuances are intentionally simplified.
- Technique IDs included in narratives are examples rather than exhaustive coverage.
- This repository does **not** redistribute the full ATT&CK corpus; it only uses short
  paraphrased clauses and technique IDs.

If you use this project in your own work, please ensure that any further use of
ATT&CK content continues to respect MITRE's licensing and trademark guidance.
