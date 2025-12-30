from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

CHROMA_DB_DIR = "chroma_db/oriental_mediclaim"
COLLECTION_NAME = "oriental_policy"

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vectorstore = Chroma(
    persist_directory=CHROMA_DB_DIR,
    embedding_function=embeddings,
    collection_name=COLLECTION_NAME
)

def retrieve_policy_clauses(query, quote_id="Q1", k=4):
    retriever = vectorstore.as_retriever(
        search_kwargs={
            "k": k,
            "filter": {"quote_id": quote_id}
        }
    )

    # ✅ CORRECT METHOD IN LANGCHAIN 0.2+
    return retriever.invoke(query)
