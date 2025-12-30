import streamlit as st
import json
from underwriting_ai import run_underwriting_analysis
from schemas import UnderwritingResult
from pydantic import ValidationError

st.set_page_config(
    page_title="Underwriting Assistant – GenAI Co-Pilot",
    layout="wide"
)

st.title("🛡️ Underwriting Assistant – GenAI Co-Pilot")

st.markdown("""
This tool assists insurance underwriters by summarizing applicant risk
using GenAI. It **does not make final underwriting decisions**.
""")

# ------------------------------
# Input Sections
# ------------------------------

with st.expander("📄 Applicant Profile (JSON)", expanded=True):
    applicant_data = st.text_area(
        "Applicant Profile",
        value=json.dumps({
            "age": 45,
            "occupation": "Construction Worker",
            "annual_income": 600000,
            "location": "Mumbai",
            "policy_type": "Health Insurance"
        }, indent=2),
        height=200
    )

with st.expander("📑 Claims History (JSON)", expanded=True):
    claims_data = st.text_area(
        "Claims History",
        value=json.dumps([
            {"year": 2022, "claim_amount": 180000, "claim_type": "Hospitalization"},
            {"year": 2023, "claim_amount": 95000, "claim_type": "Accident"}
        ], indent=2),
        height=200
    )

with st.expander("🌍 External Risk Data (JSON)", expanded=True):
    external_data = st.text_area(
        "External Risk Signals",
        value=json.dumps({
            "credit_score": 640,
            "fraud_flag": False,
            "high_risk_zone": True
        }, indent=2),
        height=200
    )

# ------------------------------
# Run Analysis
# ------------------------------

if st.button("🔍 Assess Underwriting Risk", use_container_width=True):
    try:
        result = run_underwriting_analysis(
            applicant_data,
            claims_data,
            external_data
        )

        parsed = json.loads(result)
        validated = UnderwritingResult(**parsed)

        st.success("Underwriting Risk Assessment Completed")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Risk Level", validated.risk_level)
            st.metric("Risk Score", validated.risk_score)

        with col2:
            st.markdown("### Recommendation")
            st.write(validated.recommendation)

        st.markdown("### Key Risk Factors")
        st.write(validated.key_risk_factors)

        st.markdown("### Underwriting Summary")
        st.write(validated.underwriting_summary)

    except json.JSONDecodeError:
        st.error("Model did not return valid JSON.")
    except ValidationError as e:
        st.error("Output validation failed.")
        st.text(e)
    except Exception as e:
        st.error(f"Unexpected error: {e}")
