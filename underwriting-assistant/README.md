1. Executive Summary

The Underwriting Assistant is a GenAI-powered decision-support system that assists insurance underwriters by extracting and synthesizing risk-relevant information from real underwriting documents (PDFs).

The system leverages Azure OpenAI to perform contextual reasoning over unstructured documents and generates explainable, structured underwriting insights.
It is explicitly designed as a co-pilot, ensuring that final underwriting authority remains with human experts.

2. Business Context & Problem Statement
Current Industry Challenges

Underwriting decisions rely heavily on unstructured documents

Manual review processes are:

Time-intensive

Inconsistent across underwriters

Difficult to audit at scale

Critical risk indicators are often buried across multiple PDFs

Business Impact

Increased underwriting turnaround time

Higher operational costs

Variability in risk assessment

Reduced ability to scale underwriting operations

3. Product Vision & Design Principles
Product Vision

To provide underwriters with a trusted AI co-pilot that:

Reduces document review effort

Improves risk visibility

Enhances consistency

Maintains regulatory and ethical integrity

Core Design Principles

Explainability First – Every output must be justified

Human-in-the-Loop – AI assists, humans decide

Structured Outputs – Audit-ready, machine-consumable

Enterprise Alignment – Built with regulated environments in mind

4. Functional Capabilities

📄 PDF-based underwriting workflow (industry-realistic)

🧠 Contextual risk reasoning using GenAI

📊 Risk scoring with qualitative explanations

🧾 Structured JSON output with schema validation

🛡️ Guardrails to prevent unsafe automation

🔁 Easily extensible for enterprise enhancements

5. End-to-End System Architecture
User (Underwriter)
      ↓
PDF Upload (Proposal / Claims / External Reports)
      ↓
PDF Text Extraction Layer
      ↓
Risk-Relevant Content Aggregation
      ↓
Azure OpenAI (LLM Reasoning Engine)
      ↓
Structured Risk Assessment (JSON)
      ↓
Human Review & Final Decision

6. Data Flow & Processing Logic

User uploads underwriting-related PDFs

System extracts raw text from documents

Extracted content is consolidated into a risk context

LLM performs:

Risk signal identification

Contextual reasoning

Risk scoring

Output is validated against a strict schema

Results are presented for underwriter review

7. AI Reasoning & Guardrails
AI Responsibilities

Identify underwriting risk signals

Summarize applicant risk profile

Assign a qualitative risk level

Provide transparent explanations

Explicit Guardrails

❌ No automated approvals or rejections

❌ No pricing or actuarial decisions

✅ JSON-only structured outputs

✅ Conservative, explainable reasoning

✅ Deterministic inference (low variance)

These controls align with regulated insurance environments.

8. Input & Output Specifications
Input Documents

Applicant Proposal PDF

Claims History PDF

External Risk / Credit Report PDF (Optional)

Output Schema
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


9. Technology Stack
Presentation Layer

Streamlit – Rapid UI for POC and demos

Application & Logic

Python

pdfplumber (PDF text extraction)

Pydantic (schema validation)

AI & Intelligence

Azure OpenAI

Prompt-engineered LLM workflows

Deterministic generation for consistency

Configuration & Security

Environment variables (.env)

Git-ignored secrets

Modular, maintainable codebase

10. Repository Structure
underwriting-assistant-pdf/
│
├── app.py                # Streamlit UI
├── underwriting_ai.py    # Azure OpenAI integration
├── pdf_utils.py          # PDF extraction utilities
├── schemas.py            # Output schema validation
├── requirements.txt
├── .env                  # Environment configuration (excluded)
└── .gitignore

11. Installation & Configuration
Environment Setup
pip install -r requirements.txt

Environment Variables
AZURE_OPENAI_API_KEY=***
AZURE_OPENAI_ENDPOINT=https://<resource>.openai.azure.com/
AZURE_OPENAI_API_VERSION=2024-02-15-preview
AZURE_OPENAI_DEPLOYMENT=gpt-4o

12. Usage Workflow

Launch application

Upload underwriting-related PDFs

Initiate risk assessment

Review structured AI output

Make final underwriting decision

13. Security & Compliance Considerations

No sensitive data hardcoded

No automated decision-making

Outputs are auditable and explainable

Designed for controlled internal use

Ready for integration with IAM and logging systems

14. Limitations & Assumptions

Assumes text-based PDFs (OCR not included)

Not a fraud detection engine

Not an actuarial pricing model

Intended as a decision-support tool only

15. Roadmap & Future Enhancements

OCR support for scanned documents

Vector similarity search for historical cases

Human feedback loop learning

Fraud signal correlation

Audit logging & traceability

Role-based access control

Policy-type-specific reasoning

16. Interview & Evaluation Notes
How to Position This Project

“This system demonstrates how GenAI can be responsibly applied to underwriting by assisting risk assessment through document intelligence while maintaining explainability and regulatory alignment.”

What This Project Demonstrates

Insurance domain understanding

GenAI system design

Responsible AI implementation

Enterprise architectural thinking

Final Statement

This project is intentionally designed to reflect real-world underwriting workflows, regulatory constraints, and enterprise AI best practices.
