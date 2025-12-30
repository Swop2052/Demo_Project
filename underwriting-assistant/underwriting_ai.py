import os
from dotenv import load_dotenv
from openai import AzureOpenAI

load_dotenv()

client = AzureOpenAI(
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
)

MODEL = os.getenv("AZURE_OPENAI_DEPLOYMENT")


def run_underwriting_analysis(applicant, claims, external):
    """
    Core GenAI underwriting logic
    """

    system_prompt = """
    You are an insurance underwriting assistant.
    Your job is to assess underwriting risk.

    Rules:
    - Do NOT approve or reject policies
    - ONLY assist underwriters
    - Be explainable and conservative
    - Return valid JSON ONLY
    """

    user_prompt = f"""
    Applicant Profile:
    {applicant}

    Claims History:
    {claims}

    External Risk Data:
    {external}

    Tasks:
    1. Identify underwriting risk factors
    2. Assign Risk Level: Low / Medium / High
    3. Assign Risk Score: 0–100
    4. Provide clear justification
    5. Recommend next step

    Output JSON format:
    {{
        "risk_level": "",
        "risk_score": 0,
        "key_risk_factors": [],
        "underwriting_summary": "",
        "recommendation": ""
    }}
    """

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0,
    )

    return response.choices[0].message.content
