from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
import os
from dotenv import load_dotenv

load_dotenv() 

AZURE_API_KEY = os.getenv("AZURE_OPENAI_API_KEY")
AZURE_ENDPOINT = os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_API_VERSION = os.getenv("AZURE_OPENAI_API_VERSION")
AZURE_DEPLOYMENT = os.getenv("AZURE_OPENAI_DEPLOYMENT")
# ---------------- LLM ----------------
llm = AzureChatOpenAI(
    deployment_name=AZURE_DEPLOYMENT,
    api_version=AZURE_API_VERSION,
    temperature=0.2
)

# ---------------- PROMPT ----------------
prompt = ChatPromptTemplate.from_template("""
You are an insurance assistant.

Conversation history:
{history}

User question:
{question}

Quote comparison result:
{comparison_result}

Relevant policy clauses:
{policy_clauses}

Explain clearly:
- Which quote is best
- Why
- Keep it simple
- Do not invent facts
""")

chain = prompt | llm

# ---------------- MEMORY STORE ----------------
chat_histories = {}

def get_session_history(session_id: str):
    if session_id not in chat_histories:
        chat_histories[session_id] = InMemoryChatMessageHistory()
    return chat_histories[session_id]

# ---------------- MEMORY-AWARE CHAIN ----------------
chat_chain = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="question",
    history_messages_key="history"
)

# ---------------- FUNCTION ----------------
def explain_answer(question, comparison_result, policy_docs):
    clauses_text = "\n\n".join(
        doc.page_content[:400] for doc in policy_docs
    )

    response = chat_chain.invoke(
        {
            "question": question,
            "comparison_result": comparison_result,
            "policy_clauses": clauses_text
        },
        config={"configurable": {"session_id": "insurance_chat"}}
    )

    return response.content
