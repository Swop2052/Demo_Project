from logic.quote_input import get_quotes_from_user, get_user_profile
from logic.quote_comparison import compare_quotes
from rag.retriever_chroma import retrieve_policy_clauses
from llm.explainer_with_memory import explain_answer

def chatbot():
    print("========================================")
    print(" Insurance Quote Comparison Chatbot ")
    print("========================================")

    # ---- USER INPUT ONCE ----
    quotes = get_quotes_from_user()
    user_profile = get_user_profile()

    print("\nQuotes saved. You can now ask questions.\n")

    while True:
        question = input("Ask a question (or 'exit'): ").strip()

        if question.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break

        # 1️⃣ Compare quotes
        comparison = compare_quotes(quotes, user_profile)

        # 2️⃣ RAG retrieval
        policy_docs = retrieve_policy_clauses(question)

        # 3️⃣ Explain with memory
        answer = explain_answer(
            question=question,
            comparison_result=comparison,
            policy_docs=policy_docs
        )

        print("\n--- Chatbot Response ---\n")
        print(answer)
        print("\n------------------------\n")

if __name__ == "__main__":
    chatbot()
