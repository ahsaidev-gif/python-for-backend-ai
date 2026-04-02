"""
Basic CLI for AI assistant (starting point).
"""

from utils.file_loader import load_text


def get_user_query():
    return input("Ask your question: ")


def generate_response(query):
    content = load_text("ai_project/data/sample.txt")

    if query.lower() in content.lower():
        return f"I found something related:\n{content}"

    return "No relevant information found."


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
