"""
Basic CLI for AI assistant (starting point).
"""


def get_user_query():
    return input("Ask your question: ")


def generate_response(query):
    return f"Simulated answer for: {query}"


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
