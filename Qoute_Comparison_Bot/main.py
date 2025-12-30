from rag.retriever_chroma import retrieve_policy_clauses

def main():
    print("======================================")
    print(" Insurance Policy RAG Query Interface ")
    print("======================================\n")

    while True:
        # --- USER INPUT ---
        query = input("Ask a question about the policy (or type 'exit'): ").strip()

        if query.lower() in ["exit", "quit"]:
            print("\nExiting RAG system. Goodbye!")
            break

        # --- RETRIEVE CLAUSES ---
        docs = retrieve_policy_clauses(query)

        if not docs:
            print("\nNo relevant policy clauses found.\n")
            continue

        # --- DISPLAY RESULTS ---
        print("\n--- Retrieved Policy Clauses ---\n")
        for i, doc in enumerate(docs, 1):
            print(f"Clause {i}:")
            print(doc.page_content[:600])  # limit output for readability
            print("Metadata:", doc.metadata)
            print("-" * 80)

if __name__ == "__main__":
    main()
