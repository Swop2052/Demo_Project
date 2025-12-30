from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

# -------- CONFIG --------
PDF_PATH = "data/Oriental_Mediclaim_Policy.pdf"
CHROMA_DB_DIR = "chroma_db/oriental_mediclaim"
COLLECTION_NAME = "oriental_policy"
QUOTE_ID = "Q1"

# -------- LOAD PDF --------
loader = PyPDFLoader(PDF_PATH)
documents = loader.load()

# -------- ADD METADATA --------
for doc in documents:
    doc.metadata.update({
        "quote_id": QUOTE_ID,
        "policy_name": "Oriental Mediclaim Individual",
        "source": "Oriental_Mediclaim_Policy.pdf"
    })

# -------- CHUNKING --------
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100,
    separators=["\n\n", "\n", ".", " "]
)

chunks = text_splitter.split_documents(documents)
print(f"Chunks created: {len(chunks)}")

# -------- EMBEDDINGS (MiniLM) --------
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# -------- CHROMA VECTOR STORE --------
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory=CHROMA_DB_DIR,
    collection_name=COLLECTION_NAME
)

print("ChromaDB ingestion completed successfully.")
