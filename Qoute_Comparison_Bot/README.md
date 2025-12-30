# Insurance Quote Comparison Chatbot

## Problem Statement
Users receive multiple insurance quotes in PDF format and struggle to
compare premiums, sum insured, deductibles, and claim conditions.

## Solution
This project allows users to upload multiple insurance quote PDFs and:
- Extract key financial parameters
- Compare quotes objectively
- Identify the best quote
- Ask natural-language questions using an AI assistant

## Features
- PDF parsing (Annual Premium, Sum Insured, Deductible)
- Quote comparison logic
- Best-quote recommendation
- AI-based insurance Q&A (RAG)
- Guardrails for safe responses

## Tech Stack
- Python
- Streamlit
- PDFPlumber
- Pandas
- LangChain
- OpenAI / LLM
- FAISS

## Architecture
Upload PDFs → Extract Data → Vector Store → AI Reasoning → User Output

## How to Run
1. Clone the repository
2. Install dependencies  
   `pip install -r requirements.txt`
3. Add environment variables  
   Create `.env` using `.env.example`
4. Run the app  
   `streamlit run app.py`

## Use Case
- Proof of Concept (PoC)
- Insurance domain demo
- Interview project
- Academic submission

## Future Enhancements
- OCR for scanned PDFs
- Real insurer API integration
- Policy exclusion comparison
- Risk scoring model

## Disclaimer
This is a demo system and not a certified insurance advisory tool.
