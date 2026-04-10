"""
Basic CLI for AI assistant.
"""

from llm_client import ask_llm
from retrieval.retriever import retrieve_best_chunk


def get_user_query():
    return input("Ask your question: ")


def main():
    while True:
        query = get_user_query()

        if not query.strip():
            print("Please enter a question.")
            continue

        if query.lower() == "exit":
            print("Exiting...")
            break

        try:
            # Try LLM (will fail if no API → fallback works)
            chunk = retrieve_best_chunk(query)

            if chunk:
                prompt = f"""
                Answer the question using ONLY the context below

                Context:
                {chunk}

                Question:
                {query}
                """

                response = ask_llm(prompt)
            else:
                response = "No relevant information found."

        except Exception as e:
            print("ERROR:", e)
            print("Using fallback logic...")

            chunk = retrieve_best_chunk(query)

            if chunk:
                response = f"Best match:\n{chunk}"
            else:
                response = "No relevant information found."

        print("\nAnswer:")
        print(response)


if __name__ == "__main__":
    main()
