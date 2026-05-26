# Hi, I'm Chuqian Chen

Medical AI data engineer building clinical data pipelines, LLM/RAG systems, knowledge graphs, and agentic workflows.

I work across the full path from raw healthcare data to usable intelligence: multimodal ETL, patient timelines, clinical note parsing, model-ready feature views, interpretable ML, and human-in-the-loop agent systems.

## Current Focus

- Data Engineer at USC Information Sciences Institute, building distributed ETL for multimodal healthcare data ingestion.
- AI Data R&D Engineer experience at Medin AI, building pediatric HSCT data governance and clinical note extraction systems.
- USC MS Analytics candidate, with work across Eye-AI multimodal medical data infrastructure, Mayo NIV modeling, and clinical LLM systems.
- Interested in medical AI, data engineering, LLM agents, RAG, clinical knowledge graphs, and trustworthy ML deployment.

## Experience

**USC Information Sciences Institute · Data Engineer**  
January 2025 - Present

- Engineered distributed ETL pipelines with Python and Spark UDFs for multimodal healthcare data ingestion.
- Extracted metadata and converted DICOM images to JPG, reaching about 92% data completeness.
- Optimized PostgreSQL access with partitioning and indexing.
- Collaborated with clinicians to model data relationships and build pre-aggregated ML training tables.

**Mayo Clinic · Data Scientist**  
May 2025 - August 2025

- Worked on NIV failure prediction with patient-time features, XGBoost modeling, SHAP interpretability, and prospective validation planning.

**Chinese Academy of Sciences · Full Stack Engineer**  
September 2022 - January 2024

- Built an ML-powered natural disaster alarming system.
- Developed a Django, Vue.js, and PostgreSQL web platform.
- Built a WeChat mini program for image data collection, supporting model accuracy around 90%.

## Selected Work

### HSCT Self-Evolving Data Governance

Built a clinical data processing system for pediatric hematopoietic stem cell transplant data:

- 907 patients
- 120k+ longitudinal records
- 200k+ unstructured clinical documents
- Structured patient timelines, outcome adjudication logic, prompt repair, and quality review loops

Core idea: raw data stays read-only; every transformation is versioned, auditable, and rerunnable.

### Eye-AI Multimodal Ophthalmology Platform

At USC ISI, supported a multimodal healthcare AI data platform:

- Spark/Hive data warehouse for OCT, fundus images, DICOM metadata, and clinical records
- PyDICOM image metadata parsing and preprocessing
- Multimodal sample alignment for LLM + CV modeling
- Data quality improved from 89.5% to 97.3%
- DICOM metadata extraction and JPG conversion reached about 92% data completeness

### Mayo NIV Failure Prediction

Built patient-centered time-series features and an XGBoost prediction model for NIV failure risk:

- AUC improved to 0.81
- early failure recall improved from 42% to 71%
- SHAP reports for model interpretability
- project prepared for IRB review and clinical validation

### Medical NL-to-SQL over MIMIC-IV

Designed an LLM evaluation and repair loop for clinical SQL generation:

- compared zero-shot, few-shot, and schema-constrained prompting
- evaluated DeepSeek, Qwen, Gemma, and Llama
- built BGE-M3 + FAISS dynamic schema retrieval
- added SQL syntax, execution, and error-rewrite validation

### Medinfo-extraction

LLM-driven and schema-based pipeline for medical knowledge graph construction:

- PDF / document structuring with MinerU
- entity-relation extraction
- heterogeneous entity alignment
- Neo4j graph construction
- evidence-linked relationship extraction

## Technical Stack

**Data Engineering:** Python, SQL, PostgreSQL, MongoDB, Spark, Hive, Hadoop, Presto, Airflow, DolphinScheduler  
**Analytics:** Google BigQuery, Data Visualization, R, Tableau, Power BI  
**AI / ML:** PyTorch, TensorFlow, XGBoost, scikit-learn, Hugging Face Transformers, LoRA, SHAP, BigQuery ML  
**LLM Systems:** RAG, LangChain, CrewAI, Function Calling, FAISS, BGE-M3, prompt engineering  
**Applications / Cloud:** FastAPI, Django, React, Vue, WeChat Mini Program, Docker, GCP Vertex AI, AWS, CI/CD  

## Certifications

- Lean Six Sigma White Belt Certification
- Career Essentials in Generative AI by Microsoft and LinkedIn
- Create ML Models with BigQuery ML Skill Badge
- Google Data Analytics
- Oracle Cloud Data Management 2023 Certified Foundations Associate

## What I Like Building

- reliable medical AI systems that know when to ask humans
- data pipelines that make model training reproducible
- agent workflows with validation, routing, and repair loops
- knowledge graphs that connect literature evidence with real-world patient data

## Links

- GitHub: [github.com/Chuqian-Chen](https://github.com/Chuqian-Chen)
- LinkedIn: [linkedin.com/in/chloe-chen-chuqian](https://www.linkedin.com/in/chloe-chen-chuqian)
- Email: [ccq33927@gmail.com](mailto:ccq33927@gmail.com)
