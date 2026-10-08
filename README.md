<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/hero-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/hero-light.svg">
  <img alt="Chuqian Chen — clinical AI that refuses to guess" src="./assets/hero-light.svg" width="100%">
</picture>

**English** · [中文](README.zh-CN.md)

<a href="mailto:ccq33927@gmail.com"><img alt="Email" src="https://img.shields.io/badge/Email-0E3B34?style=flat-square&logo=gmail&logoColor=white"></a>
<a href="https://www.linkedin.com/in/chloe-chen-chuqian"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-0E3B34?style=flat-square&logo=linkedin&logoColor=white"></a>
<a href="https://leetcode.com/u/chuqianc/"><img alt="LeetCode" src="https://img.shields.io/badge/LeetCode-0E3B34?style=flat-square&logo=leetcode&logoColor=white"></a>

I work on the layer between messy clinical data and decisions people are willing to act on:
ontologies over population biobanks, knowledge-graph evidence retrieval, and health agents that fall
back to deterministic rules when the LLM is off. Most of what I ship runs with zero API keys, carries
a disclaimer on every response, and declines to answer when the evidence isn't there.

**Now** &nbsp;AI Data R&D at **Fudan University**, through its industry–academia partner company — a self-evolving
health agent and a Palantir-style ontology over UK Biobank. On the side, 400+ LeetCode problems and a 1800+ contest rating.

<br>


`algorithms` &nbsp;400+ LeetCode · 1800+ contest rating · dynamic programming, graphs, DP on trees &nbsp;·&nbsp; [global](https://leetcode.com/u/chuqianc/) / [cn](https://leetcode.cn/u/ccq33927/)

**How I build** &nbsp;Never diagnose · never invent data · evidence or nothing · prove the checks work.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/system-map-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/system-map-light.svg">
  <img alt="From raw signal to a reviewed decision, and back" src="./assets/system-map-light.svg" width="100%">
</picture>

## Machine learning

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/methods-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/methods-light.svg">
  <img alt="Machine learning methods and the number each one defends" src="./assets/methods-light.svg" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/eval-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/eval-light.svg">
  <img alt="Retrieval evaluation against baselines with bootstrap CIs, and leave-one-axis-out stability" src="./assets/eval-light.svg" width="100%">
</picture>

Retrieval evaluated against an age–sex baseline and a single-axis baseline with paired-bootstrap intervals; leave-one-axis-out stability before and after calibration. Read straight from `retrieval_eval.json` and `loo_stability.json`.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/kg-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/kg-light.svg">
  <img alt="Indicator association network drawn from the ontology's knowledge graph" src="./assets/kg-light.svg" width="100%">
</picture>

The ontology's indicator network, drawn from its own `knowledge_graph.json`: Spearman ρ between axes, Cohen's d between disease chapters and phenotypes. Every edge carries an evidence grade; sex-skewed case groups are excluded.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/niv-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/niv-light.svg">
  <img alt="NIV failure model: SHAP feature importance and model card" src="./assets/niv-light.svg" width="100%">
</picture>

Gradient-boosted NIV-failure model from the Mayo Clinic work: SHAP importances read from the repository's own export, and the model card as implemented — timepoint-anchored labels, grouped cross-validation by ICU stay, isotonic calibration, an operating point chosen for PPV ≥ 0.30 at recall ≥ 0.80.

## Selected systems

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/card-ukb-agent-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/card-ukb-agent-light.svg">
  <img alt="Self-evolving health agent over UK Biobank" src="./assets/card-ukb-agent-light.svg" width="100%">
</picture>

**Fudan University** · industry–academia partner company · 2026<br>

Lab reports (PDF, photo, xlsx, HEIC), wearables, CGM, blood pressure, handheld ultrasound and EEG / fMRI / fNIRS,
parsed into one ontology-backed profile and compared against ~500k UK Biobank norms. Published risk models,
12-hallmark aging, six-state drug-toxicity monitoring, and an intervention planner gated by a deterministic
safety check. With no API key configured, the rule engine answers alone.<br>
`FastAPI` `vanilla ES modules` `SQLite` `Playwright` `ruff → lock → pytest → E2E CI`

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/card-ontology-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/card-ontology-light.svg">
  <img alt="A Palantir-style ontology over 498,339 people" src="./assets/card-ontology-light.svg" width="100%">
</picture>

**Fudan University** · industry–academia partner company · 2026<br>

26 object types, 13 interfaces, 38 link types and 15 actions over 11,318 UK Biobank fields, grouped by the
official dictionary rather than by guess. Missing-aware similarity across eight data layers with 10–100%
coverage; compiles to GraphQL SDL, property-graph and JSON Schema; term reuse audited against FHIR R5 and
OMOP CDM. A self-contained HTML explorer draws all of it — and drawing it caught four schema bugs the text audits missed.<br>
`Parquet` `YAML schema` `Python` `85 CI checks` `100 fault-injection cases` `CQ suite 70%`

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/ontology-tiers-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/ontology-tiers-light.svg">
  <img alt="Ontology tiers: master data, process events, derived results" src="./assets/ontology-tiers-light.svg" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/retrieval-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/retrieval-light.svg">
  <img alt="Similar-patient retrieval algorithm over 498,339 people" src="./assets/retrieval-light.svg" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/card-women-health-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/card-women-health-light.svg">
  <img alt="Supplement advice with a full evidence chain" src="./assets/card-women-health-light.svg" width="100%">
</picture>

**Independent project** · solo-built · 2026<br>

Local-first WeChat mini program plus FastAPI backend. Lifestyle answers alone drive recommendations; every
card expands to the user facts, the SHA256-signed source document, and the NIH / FDA / NCCIH evidence behind
it. Batch OCR of order screenshots; idempotent three-step checkout with a server-side clinical gate that
returns 422 under any risk context, whatever the UI does.<br>
`WeChat Mini Program` `FastAPI` `SQLAlchemy 2` `SQLite` `24 API tests`

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/card-hsct-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/card-hsct-light.svg">
  <img alt="Transplant risk explained, probability untouched" src="./assets/card-hsct-light.svg" width="100%">
</picture>

**Medin AI** · AI Data R&D · 2026<br>

Takes an individual probability from any upstream model, retrieves evidence from a literature graph and a
903-patient EHR cohort graph for seven HSCT outcomes, and grades evidence sufficiency instead of comparing
incompatible probabilities. Per-outcome clinical windows; transplant-specific risk factors (HLA mismatch,
conditioning intensity, CMV serology, CD34 dose). Neo4j when reachable, local Parquet when not.<br>
`FastAPI` `Neo4j` `Parquet` `GRU-D DeepHit adapter` `controlled prompts` `demo predictions hard-flagged`

<details>
<summary><b>Also on the shelf</b></summary>

<br>

**[preprocess-ui](https://github.com/Chuqian-Chen/preprocess-ui)** — local, offline-capable data-quality
workbench for messy CSV: profile fields, detect table relationships, review AI-proposed cleaning as JSON
operations before anything is applied, diff raw vs processed distributions.

**[langgraph-agent-demo](https://github.com/Chuqian-Chen/langgraph-agent-demo)** — the LangGraph overview
reduced to a runnable, unit-tested graph with a deterministic mock LLM.

</details>

<details>
<summary><b>Earlier research</b></summary>

<br>

**Eye-AI multimodal ophthalmology platform** (USC ISI) — Spark / Hive warehouse over 200k+ OCT and fundus
images, DICOM metadata and structured records; PyDICOM conversion, high-throughput PostgreSQL access,
92% data completeness after quality rules.

**NIV → IMV escalation predictor** (Mayo Clinic) — HACOR score at 1 / 6 / 12 / 24 h plus vitals from eICU-CRD and
MIMIC-IV; XGBoost with class weighting, GroupKFold by ICU stay, isotonic calibration, SHAP; Streamlit app with
cohort filters, phenotypes and a case explorer. Internal validation only — no held-out test set yet, so no headline AUC is claimed.

**Medical NL-to-SQL over MIMIC-IV** — DeepSeek / Qwen / Gemma / Llama comparison, BGE-M3 + FAISS schema
retrieval, SQL verification and rewrite loop. 83% JOIN accuracy.

**Clinical document extraction** — 200k+ documents parsed; 96.2% accuracy on toxicity labels.

</details>

## Stack

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/stack-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/stack-light.svg">
  <img alt="Stack" src="./assets/stack-light.svg" width="100%">
</picture>

## Experience

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/timeline-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/timeline-light.svg">
  <img alt="Experience timeline 2022 to 2026" src="./assets/timeline-light.svg" width="100%">
</picture>

<details>
<summary><b>Certifications</b></summary>

<br>

AWS Certified Cloud Practitioner &nbsp;·&nbsp; Salesforce AI Associate &nbsp;·&nbsp; Google Data Analytics &nbsp;·&nbsp;
Create ML Models with BigQuery ML &nbsp;·&nbsp; Oracle Cloud Data Management 2023 Foundations Associate &nbsp;·&nbsp;
Career Essentials in Generative AI (Microsoft / LinkedIn) &nbsp;·&nbsp; Lean Six Sigma White Belt

</details>

## Verification

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/verification-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/verification-light.svg">
  <img alt="What runs green before anything ships" src="./assets/verification-light.svg" width="100%">
</picture>

## Contact

Open to work in medical AI, data engineering, ML systems, and LLM / agent development.

[Email](mailto:ccq33927@gmail.com) &nbsp;·&nbsp; [LinkedIn](https://www.linkedin.com/in/chloe-chen-chuqian) &nbsp;·&nbsp; [LeetCode](https://leetcode.com/u/chuqianc/) &nbsp;·&nbsp; [LeetCode CN](https://leetcode.cn/u/ccq33927/)
