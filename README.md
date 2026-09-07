<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/hero-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/hero-light.svg">
  <img alt="Chuqian Chen — clinical AI that refuses to guess" src="./assets/hero-light.svg" width="100%">
</picture>

<a href="mailto:ccq33927@gmail.com"><img alt="Email" src="https://img.shields.io/badge/Email-0E3B34?style=flat-square&logo=gmail&logoColor=white"></a>
<a href="https://www.linkedin.com/in/chloe-chen-chuqian"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-0E3B34?style=flat-square&logo=linkedin&logoColor=white"></a>
<a href="https://leetcode.com/u/chuqianc/"><img alt="LeetCode" src="https://img.shields.io/badge/LeetCode-0E3B34?style=flat-square&logo=leetcode&logoColor=white"></a>

I work on the layer between messy clinical data and decisions people are willing to act on:
ontologies over population biobanks, knowledge-graph evidence retrieval, and health agents that fall
back to deterministic rules when the LLM is off. Most of what I ship runs with zero API keys, carries
a disclaimer on every response, and declines to answer when the evidence isn't there.

**Now** &nbsp;AI Data R&D at **Medin AI** — a self-evolving health agent and a Palantir-style ontology over
UK Biobank. On the side, 400+ LeetCode problems and a 1800+ contest rating.

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/principles-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/principles-light.svg">
  <img alt="Four rules every system I ship obeys: never diagnose, never invent data, evidence or nothing, prove the checks work" src="./assets/principles-light.svg" width="100%">
</picture>

## Selected systems

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/card-ukb-agent-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/card-ukb-agent-light.svg">
  <img alt="Self-evolving health agent over UK Biobank" src="./assets/card-ukb-agent-light.svg" width="100%">
</picture>

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

26 object types, 13 interfaces, 38 link types and 15 actions over 11,318 UK Biobank fields, grouped by the
official dictionary rather than by guess. Missing-aware similarity across eight data layers with 10–100%
coverage; compiles to GraphQL SDL, property-graph and JSON Schema; term reuse audited against FHIR R5 and
OMOP CDM. A self-contained HTML explorer draws all of it — and drawing it caught four schema bugs the text audits missed.<br>
`Parquet` `YAML schema` `Python` `85 CI checks` `100 fault-injection cases` `CQ suite 70%`

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/card-hsct-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/card-hsct-light.svg">
  <img alt="Transplant risk explained, probability untouched" src="./assets/card-hsct-light.svg" width="100%">
</picture>

Takes an individual probability from any upstream model, retrieves evidence from a literature graph and a
903-patient EHR cohort graph for seven HSCT outcomes, and grades evidence sufficiency instead of comparing
incompatible probabilities. Per-outcome clinical windows; transplant-specific risk factors (HLA mismatch,
conditioning intensity, CMV serology, CD34 dose). Neo4j when reachable, local Parquet when not.<br>
`FastAPI` `Neo4j` `Parquet` `GRU-D DeepHit adapter` `controlled prompts` `demo predictions hard-flagged`

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="./assets/card-women-health-dark.svg">
  <source media="(prefers-color-scheme: light)" srcset="./assets/card-women-health-light.svg">
  <img alt="Supplement advice with a full evidence chain" src="./assets/card-women-health-light.svg" width="100%">
</picture>

Local-first WeChat mini program plus FastAPI backend. Lifestyle answers alone drive recommendations; every
card expands to the user facts, the SHA256-signed source document, and the NIH / FDA / NCCIH evidence behind
it. Batch OCR of order screenshots; idempotent three-step checkout with a server-side clinical gate that
returns 422 under any risk context, whatever the UI does.<br>
`WeChat Mini Program` `FastAPI` `SQLAlchemy 2` `SQLite` `24 API tests`

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

**NIV failure prediction** (Mayo Clinic) — patient-time ICU respiratory features, XGBoost with SMOTE and
class weighting, SHAP reports. AUC 0.81; early-failure recall lifted to 71%.

**Medical NL-to-SQL over MIMIC-IV** — DeepSeek / Qwen / Gemma / Llama comparison, BGE-M3 + FAISS schema
retrieval, SQL verification and rewrite loop. 83% JOIN accuracy.

**Clinical document extraction** — 200k+ documents parsed; 96.2% accuracy on toxicity labels.

</details>

## Stack

- **Languages** &nbsp;`Python` `Java` `TypeScript` `JavaScript` `SQL`
- **Data** &nbsp;`Spark` `Hive` `Hadoop` `Parquet` `PostgreSQL` `BigQuery` `Neo4j` `Redis` `MongoDB`
- **ML** &nbsp;`PyTorch` `TensorFlow` `XGBoost` `SHAP` `LoRA` `RoBERTa` `GRU-D`
- **LLM & agents** &nbsp;`LangGraph` `RAG` `NL-to-SQL` `FAISS` `BGE-M3` `MinerU` `constrained decoding`
- **Ontology** &nbsp;`Palantir-style object model` `FHIR R5` `OMOP CDM` `GraphQL SDL` `JSON Schema`
- **Services** &nbsp;`FastAPI` `Django` `Spring Boot` `Flask` `Node.js` `React` `Vue` `WeChat Mini Program`
- **Infra** &nbsp;`Docker` `Kubernetes` `MLflow` `Kubeflow` `Playwright` `AWS` `GCP`

## Experience

| Year | Where | Role |
| :-- | :-- | :-- |
| **2026** | Medin AI | AI Data R&D — UK Biobank health agent, medical ontology, HSCT explainability |
| **2025** | Mayo Clinic | Data Scientist — NIV failure prediction |
| **2025** | USC Information Sciences Institute | Data Engineer — Eye-AI multimodal health data |
| **2024** | University of Southern California | MS Analytics |
| **2022** | Chinese Academy of Sciences | Full Stack Engineer — ML disaster alarming system |

<details>
<summary><b>Certifications</b></summary>

<br>

AWS Certified Cloud Practitioner &nbsp;·&nbsp; Salesforce AI Associate &nbsp;·&nbsp; Google Data Analytics &nbsp;·&nbsp;
Create ML Models with BigQuery ML &nbsp;·&nbsp; Oracle Cloud Data Management 2023 Foundations Associate &nbsp;·&nbsp;
Career Essentials in Generative AI (Microsoft / LinkedIn) &nbsp;·&nbsp; Lean Six Sigma White Belt

</details>

## GitHub

<p>
  <img height="150" alt="GitHub stats" src="https://github-readme-stats.vercel.app/api?username=Chuqian-Chen&show_icons=true&hide_border=true&rank_icon=github&bg_color=00000000&title_color=4F9A87&icon_color=B8724A&text_color=8A8378">
  <img height="150" alt="Top languages" src="https://github-readme-stats.vercel.app/api/top-langs/?username=Chuqian-Chen&layout=compact&hide_border=true&bg_color=00000000&title_color=4F9A87&text_color=8A8378">
</p>

## Contact

Open to work in medical AI, data engineering, ML systems, and LLM / agent development.

[Email](mailto:ccq33927@gmail.com) &nbsp;·&nbsp; [LinkedIn](https://www.linkedin.com/in/chloe-chen-chuqian) &nbsp;·&nbsp; [LeetCode](https://leetcode.com/u/chuqianc/) &nbsp;·&nbsp; [LeetCode CN](https://leetcode.cn/u/ccq33927/)
