"""
Basic CLI for AI assistant (starting point).
"""


def get_user_query():
    return input("Ask your question: ")


def generate_response(query):
    query = query.lower()

    if "python" in query:
        return "Python is widely used in backend development and AI systems."

    elif "ai" in query or "artificial intelligence" in query:
        return "AI enables machines to simulate human intelligence like learning and reasoning."

    elif "rag" in query:
        return " RAG (Retrieval-Augmented Generation) combines seacrh with LLMs to give accurate answers."

    else:
        return "I am still learning. Please ask about Python, AI, or RAG."


def main():
    while True:
        query = get_user_query()

        if query.lower() == "exit":
            break

        response = generate_response(query)

        print("\nAnswer:")
        print(response)


if __name__ == "__main__":
    main()
