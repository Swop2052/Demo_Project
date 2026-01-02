# Underwriting Assistant: GenAI-Powered Decision Support System

## 1. Overview
The Underwriting Assistant is an enterprise-grade, AI-enhanced decision-support platform designed for insurance professionals. It processes unstructured underwriting documents (PDFs) to extract, analyze, and present risk-relevant insights, enabling faster and more consistent risk assessments while ensuring human oversight remains central to all final decisions.

## 2. Business Context & Problem Statement
Industry Challenges
Underwriting decisions depend heavily on manual review of unstructured documents

## Current processes are:

Time-intensive – hours spent per case on document review
Inconsistent – variability across different underwriters
Hard to audit – lack of structured, machine-readable audit trails
Critical risk indicators are often buried across multiple PDFs

## Business Impact
Increased underwriting turnaround time
Higher operational costs due to manual effort
Variable risk assessment quality
Limited scalability of underwriting operations

## 3. System Architecture
```text
┌─────────────────┐
│   User          │
│  (Underwriter)  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  PDF Upload     │
│  (Proposal / Claims │
│   / External Reports)│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  PDF Text       │
│  Extraction Layer│
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Risk-Relevant  │
│  Content        │
│  Aggregation    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Azure OpenAI   │
│  (LLM Reasoning │
│   Engine)       │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Structured Risk│
│  Assessment     │
│  (JSON Output)  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Human Review   │
│  & Final Decision│
└─────────────────┘
```

## 4. Core Capabilities
## Feature	                   ##Description
📄 PDF-Based Workflow	       Industry-realistic document processing pipeline
🧠 Contextual Risk Reasoning	 GenAI-powered analysis of document context
📊 Risk Scoring	Qualitative  scoring with detailed explanations
🧾 Structured JSON Output	 Validated, machine-consumable results
🛡️ Enterprise Guardrails	 Built-in safety and compliance controls
🔁 Extensible Design	       Modular architecture for easy enhancement

## 5. AI Reasoning & Safety Controls
AI Responsibilities
Identify underwriting risk signals across documents
Summarize applicant risk profile holistically
Assign qualitative risk levels (Low/Medium/High)
Provide transparent, document-referenced explanations

## Explicit Guardrails
❌ No automated approvals or rejections
❌ No pricing or actuarial decisions
✅ JSON-only structured outputs (no free-form decisions)
✅ Conservative reasoning approach
✅ Deterministic inference (low variance for consistency)

## 6. Input/Output Specifications
Supported Input Documents
Applicant Proposal PDF
Claims History PDF
External Risk/Credit Report PDF (Optional)

## Output Schema
```text
{
  "risk_level": "Medium",
  "risk_score": 62,
  "key_risk_factors": [
    "Prior hospitalization claims",
    "Moderate credit score",
    "Urban high-risk location"
  ],
  "underwriting_summary": "The applicant presents moderate underwriting risk primarily driven by claims history.",
  "recommendation": "Proceed with detailed manual review"
}
```

## 7. Technology Stack
Presentation Layer
Streamlit – Rapid UI for POC and demonstration

Application & Logic
Python – Core application logic
pdfplumber – PDF text extraction
Pydantic – Schema validation and data modeling

AI & Intelligence
Azure OpenAI – LLM reasoning engine
Prompt Engineering – Domain-specific optimization
Deterministic Generation – Consistent outputs

Configuration & Security
Environment variables (.env)
Git-ignored secrets management
Modular, maintainable codebase

## 8. Repository Structure
```text
underwriting-assistant-pdf/
│
├── app.py                 # Streamlit UI and application flow
├── underwriting_ai.py     # Azure OpenAI integration and reasoning
├── pdf_utils.py           # PDF extraction and text processing
├── schemas.py             # Pydantic models for output validation
├── requirements.txt       # Python dependencies
├── .env                   # Environment configuration (git-ignored)
└── .gitignore            # Security and environment exclusions
```
## 9. Installation & Setup
Prerequisites
Python 3.9+
Azure OpenAI resource with GPT-4 deployment
Valid API credentials

## Installation Steps
```text
# Clone repository
git clone <repository-url>
cd underwriting-assistant-pdf

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your Azure OpenAI credentials
```
## 10. Usage Workflow
Launch Application
```text
streamlit run app.py
```
## Upload Documents
Drag and drop underwriting-related PDFs
Supported: Proposals, Claims History, Risk Reports

## Initiate Analysis
Click "Assess Risk" to process documents
System extracts text and runs AI reasoning

## Review Results
Examine structured risk assessment
Review key risk factors and explanations

## Make Decision
Use AI insights to inform manual review
Maintain final underwriting authority

## Note: 
This system is intentionally designed to reflect real-world underwriting workflows, regulatory constraints, and enterprise AI best practices. It serves as both a functional tool and a reference implementation for responsible GenAI adoption in regulated industrie






















