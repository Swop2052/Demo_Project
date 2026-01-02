# 🛡️ Insurance Quote Comparison Chatbot
AI-Powered Insurance Quote Intelligence Platform

## 📌 Overview
The Insurance Quote Comparison Chatbot is an AI-driven application that analyzes, compares, and explains insurance quotes using structured data extraction, document intelligence, and Large Language Models (LLMs). Designed as a proof-of-concept (PoC), it mirrors real-world insurance underwriting and advisory workflows by enabling users to upload multiple insurance quote PDFs, extract key financial parameters, and receive:

A side-by-side comparison of quotes
An AI-recommended best quote based on configurable preferences
Natural-language explanations tailored to user questions

## 🎯 Problem Statement
Insurance quotes are often complex, inconsistent across insurers, and difficult for customers to interpret. Users struggle to understand:-
Which quote offers better value
Trade-offs between premium, coverage, and deductible
Hidden implications within policy documents

This solution bridges that gap by:-

Structuring unstructured insurance PDFs
Standardizing comparison metrics
Using AI to explain decisions transparently

## 🚀 Key Features
## Feature	                                  ## Description
Quote Comparison Engine	                  Supports multiple insurance quotes; extracts and compares Sum Insured, Annual Premium, Deductible,                                                       and normalizes values for fair evaluation

PDF Intelligence (RAG)	                   Reads real insurance quote documents using Retrieval-Augmented Generation (RAG) with ChromaDB; ensures answers                                           are grounded in actual policy text

AI Chatbot (Explainability Layer)	        Accepts natural questions (e.g., “Which quote is best for low deductible?”); responds using policy-aware                                                 reasoning

Memory-Aware Conversations	              Retains context across user interactions; enables follow-up questions without re-uploading data

Audit & Logging	                          Timestamped logs for user actions and AI responses; supports compliance and traceability

## 🧠 Architecture
```text
graph TD
    A[User Uploads PDFs] --> B[PDF Parser (pdfplumber)]
    B --> C[Structured Quote Extraction]
    C --> D[Comparison Logic Engine]
    D --> E[RAG (ChromaDB) Retrieval]
    E --> F[Azure OpenAI LLM]
    F --> G[Chatbot Explanation]
```

## 🗂️ Project Structure
```text
Qoute_Comparison_Bot/
│
├── main.py                     # Application entry point
├── chatbot.py                  # User interaction & chat logic
│
├── logic/
│   ├── quote_input.py          # Quote ingestion & validation
│   └── quote_comparison.py     # Comparison and scoring logic
│
├── llm/
│   └── explainer_with_memory.py # AI explanation + conversation memory
│
├── rag/
│   ├── ingest_chroma.py        # PDF ingestion into vector DB
│   └── retriever_chroma.py     # Context retrieval for LLM
│
├── data/
│   └── Oriental_Mediclaim_Policy.pdf  # Sample insurance document
│
├── logs/
│   └── audit_logs.csv          # User & AI interaction logs
│
├── .env                        # Environment variables (not committed)
├── .gitignore
└── README.md
```

## 🧾 Comparison Parameters (Industry-Relevant)
## Parameter	                ## Description
Annual Premium	              Yearly cost paid by the customer
Sum Insured	                 Maximum claim payout
Deductible	                  Amount paid by user before insurer pays
Value Score	                 AI-derived score balancing cost vs coverage
Risk Notes	                  AI explanation of trade-offs

## 🔐 Environment Configuration
Create a .env file in the root directory with the following

## 🧪 Getting Started
```text
1️ Clone the Repository
bash
git clone https://github.com/your-username/Insurance-Quote-Comparison.git
cd Qoute_Comparison_Bot

2️ Create Virtual Environment
bash
python -m venv venv
On Windows:
venv\Scripts\activate
On macOS/Linux:
source venv/bin/activate

3️ Install Dependencies
bash
pip install -r requirements.txt

4️ Run the Application
bash
python main.py
```
## 🛡️ Guardrails & Safety
Responses are grounded in retrieved policy text (RAG) to minimize hallucinations
All user and AI interactions are logged for traceability
Explicit disclaimers are provided (AI ≠ licensed insurance advisor)

## Disclaimer
This project is for educational and demonstration purposes only.
It does not provide financial or insurance advice. Always consult a licensed professional for insurance decisions.


















