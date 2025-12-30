import os
import streamlit as st
import pandas as pd
import pdfplumber
from dotenv import load_dotenv
from openai import AzureOpenAI
from datetime import datetime
from pandas.errors import EmptyDataError

# =========================================================
# ENVIRONMENT
# =========================================================
load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION")
)

MODEL = os.getenv("AZURE_OPENAI_DEPLOYMENT")

# =========================================================
# CONFIGURATION
# =========================================================
st.set_page_config(
    page_title="Insurance Claims Intelligence Platform",
    layout="wide"
)

LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "audit_logs.csv")
os.makedirs(LOG_DIR, exist_ok=True)

REQUIRED_COLUMNS = {
    "timestamp", "claim_type", "decision",
    "appeal_score", "human_review"
}

CLAIM_TYPES = [
    "Health", "Motor", "Life", "Travel",
    "Home / Property", "Commercial",
    "Personal Accident"
]

LANGUAGES = ["English", "Hindi", "Marathi"]

# =========================================================
# DOCUMENT EXTRACTION
# =========================================================
def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text.strip()

# =========================================================
# CLAIM DECISION DETECTION
# =========================================================
def detect_claim_decision(report):
    r = report.lower()
    if "rejected" in r or "not payable" in r:
        return "Denied"
    if "partially approved" in r or "partial approval" in r:
        return "Partially Approved"
    if "approved" in r:
        return "Approved"
    return "Unclear"

# =========================================================
# PROMPTS
# =========================================================
def explanation_prompt(claim_type, decision, report, language):
    return f"""
You are an insurance claims explanation assistant.

Claim Type: {claim_type}
Decision (as stated in document): {decision}
Language: {language}

RULES:
- Use ONLY information present in the claim report.
- Do NOT invent policy rules.
- Do NOT promise outcomes or approvals.
- If information is missing, say so clearly.

FORMAT:

1. Claim Decision
2. Why This Decision Was Made
3. What This Means for You
4. What You Can Do Next

Claim Report:
\"\"\"{report}\"\"\"
"""

def domain_bot_prompt(report, question):
    return f"""
You are an insurance domain assistant.

PRIORITY RULES:
1. First use the uploaded claim report.
2. If the answer is not in the report, you MAY use general insurance knowledge.
3. Clearly say when general knowledge is used.
4. Do NOT provide legal or financial advice.

Claim Report:
\"\"\"{report}\"\"\"

User Question:
{question}
"""

def hallucination_guard(report, explanation):
    return f"""
Check whether the explanation is fully supported by the claim report.
Reply strictly YES or NO.

Report:
{report}

Explanation:
{explanation}
"""

def appeal_score_prompt(report):
    return f"""
Based ONLY on the claim report,
estimate appeal success likelihood between 0 and 1.
Return only a numeric value.

{report}
"""

# =========================================================
# LLM CALL
# =========================================================
def call_llm(prompt):
    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3
    )
    return response.choices[0].message.content.strip()

# =========================================================
# GOVERNANCE FUNCTIONS
# =========================================================
def hallucination_check(report, explanation):
    result = call_llm(hallucination_guard(report, explanation))
    return "YES" in result.upper()

def appeal_score(report):
    try:
        return float(call_llm(appeal_score_prompt(report)))
    except:
        return 0.0

def log_event(claim_type, decision, score, reviewed):
    row = {
        "timestamp": datetime.now(),
        "claim_type": claim_type,
        "decision": decision,
        "appeal_score": score,
        "human_review": reviewed
    }
    df = pd.DataFrame([row])

    if not os.path.exists(LOG_FILE) or os.stat(LOG_FILE).st_size == 0:
        df.to_csv(LOG_FILE, index=False)
    else:
        df.to_csv(LOG_FILE, mode="a", header=False, index=False)

# =========================================================
# UI
# =========================================================
st.title("Insurance Claims Intelligence Platform")

tab1, tab2, tab3 = st.tabs([
    "Claim Explanation",
    "Insurance Q&A Bot",
    "Audit & Analytics"
])

# =========================================================
# TAB 1 – CLAIM EXPLANATION BOT
# =========================================================
with tab1:
    claim_type = st.selectbox("Claim Type", CLAIM_TYPES)
    language = st.selectbox("Explanation Language", LANGUAGES)

    report = st.text_area("Paste Claim Report", height=220)
    pdf = st.file_uploader("Upload Claim PDF", type=["pdf"])

    if pdf:
        report = extract_text_from_pdf(pdf)
        st.info("Claim report extracted successfully.")

    if st.button("Generate Claim Explanation"):
        if not report.strip():
            st.warning("Claim report is required.")
        else:
            decision = detect_claim_decision(report)
            explanation = call_llm(
                explanation_prompt(claim_type, decision, report, language)
            )

            valid = hallucination_check(report, explanation)
            score = appeal_score(report)

            st.subheader("Detected Claim Decision")
            st.write(decision)

            st.subheader("Explanation")
            st.write(explanation)

            st.caption(
                "Disclaimer: This explanation is for understanding purposes only "
                "and does not replace the official claim decision or policy document."
            )

            st.subheader("Appeal Readiness Score")
            st.progress(score)

            reviewed = False
            if not valid or score < 0.6:
                reviewed = st.checkbox("Flag for human review")

            log_event(claim_type, decision, score, reviewed)

# =========================================================
# TAB 2 – INSURANCE DOMAIN Q&A BOT
# =========================================================
with tab2:
    st.subheader("Insurance Q&A Assistant")

    if "qa_history" not in st.session_state:
        st.session_state.qa_history = []

    user_q = st.text_input("Ask a question related to your claim or insurance")

    if st.button("Ask"):
        if not report.strip():
            st.warning("Upload or paste a claim report first.")
        else:
            answer = call_llm(domain_bot_prompt(report, user_q))
            st.session_state.qa_history.append((user_q, answer))

    for q, a in st.session_state.qa_history:
        st.markdown(f"**User:** {q}")
        st.markdown(f"**Bot:** {a}")

# =========================================================
# TAB 3 – AUDIT & ANALYTICS
# =========================================================
with tab3:
    st.subheader("Audit Logs & Analytics")

    if not os.path.exists(LOG_FILE):
        st.info("No audit data available.")
    else:
        try:
            df = pd.read_csv(LOG_FILE)
            if df.empty:
                st.info("Audit log is empty.")
            elif not REQUIRED_COLUMNS.issubset(df.columns):
                st.error("Audit schema mismatch.")
            else:
                st.dataframe(df)
                st.bar_chart(
                    df.groupby("decision")["appeal_score"].mean()
                )
        except EmptyDataError:
            st.info("Audit log is empty.")
