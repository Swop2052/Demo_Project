🛡️ Insurance Quote Comparison Chatbot

AI-Powered Insurance Quote Intelligence Platform

📌 Project Overview

The Insurance Quote Comparison Chatbot is an AI-driven application designed to analyze, compare, and explain insurance quotes using structured data extraction, document intelligence, and Large Language Models (LLMs).

This platform enables users to upload multiple insurance quote PDFs, extract key financial parameters, and receive:

A side-by-side comparison

An AI-recommended best quote

Natural-language explanations tailored to user questions

The solution is built as a proof-of-concept (PoC) that closely mirrors real-world insurance underwriting and advisory workflows.

🎯 Problem Statement

Insurance quotes are often:

Complex

Inconsistent across insurers

Difficult for customers to interpret

Users struggle to understand:

Which quote offers better value

Trade-offs between premium, coverage, and deductible

Hidden implications within policy documents

This project solves that gap by:

Structuring unstructured insurance PDFs

Standardizing comparison metrics

Using AI to explain decisions transparently

🚀 Key Features
✅ Quote Comparison Engine

Supports multiple insurance quotes

Extracts and compares:

Sum Insured

Annual Premium

Deductible

Normalizes values for fair evaluation

✅ PDF Intelligence (RAG)

Reads real insurance quote documents

Uses Retrieval-Augmented Generation (RAG) with ChromaDB

Ensures answers are grounded in actual policy text

✅ AI Chatbot (Explainability Layer)

Ask natural questions such as:

“Which quote is best for low deductible?”

“Why is Quote B cheaper?”

AI responds using policy-aware reasoning

✅ Memory-Aware Conversations

Retains context across user interactions

Enables follow-up questions without re-uploading data

✅ Audit & Logging

Timestamped logs for:

User actions

AI responses

Supports compliance and traceability

🧠 Architecture Overview
User
 └── Upload Insurance PDFs
      └── PDF Parser (pdfplumber)
           └── Structured Quote Extraction
                └── Comparison Logic
                     └── RAG (ChromaDB)
                          └── Azure OpenAI (LLM)
                               └── Chatbot Explanation

🗂️ Project Structure
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

🧾 Comparison Parameters (Industry-Relevant)
Parameter	Description
Annual Premium	Yearly cost paid by the customer
Sum Insured	Maximum claim payout
Deductible	Amount paid by user before insurer pays
Value Score	AI-derived score balancing cost vs coverage
Risk Notes	AI explanation of trade-offs
🔐 Environment Configuration

Create a .env file in the root directory:

AZURE_OPENAI_API_KEY=your_api_key
AZURE_OPENAI_ENDPOINT=https://your-endpoint.openai.azure.com/
AZURE_OPENAI_API_VERSION=2024-02-15-preview
AZURE_OPENAI_DEPLOYMENT=your-deployment-name


⚠️ Never commit .env files to GitHub.

🧪 How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/your-username/Insurance-Quote-Comparison.git
cd Qoute_Comparison_Bot

2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
python main.py

📊 Use Case Scenarios

Insurance advisors comparing plans for customers

Customers evaluating multiple policy offers

Underwriting PoC demonstrations

AI explainability showcase for interviews

🛡️ Guardrails & Safety

Responses grounded in retrieved policy text (RAG)

No hallucinated policy details

Logged interactions for traceability

Explicit disclaimers (AI ≠ licensed advisor)

📈 Project Status

✅ Proof-of-Concept (PoC)
🚧 Not production-ready

Production Enhancements Needed:

Authentication & role-based access

Secure document storage

Policy versioning

Regulatory compliance checks (IRDAI, GDPR)

UI enhancements

🎯 Interview & Resume Value

This project demonstrates:

Applied GenAI (LLMs + RAG)

Real-world insurance domain understanding

Explainable AI

End-to-end system design

Enterprise-style project structuring

Highly suitable for AI, Data, and GenAI interviews.

📌 Disclaimer

This project is for educational and demonstration purposes only.
It does not provide financial or insurance advice.

👤 Author

Swapnil Ingle
AI / GenAI Project Portfolio
