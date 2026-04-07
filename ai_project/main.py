"""
Basic CLI for AI assistant (starting point).
"""

from utils.file_loader import load_text, split_into_chunks


def get_user_query():
    return input("Ask your question: ")


def generate_response(query):
    content = load_text("ai_project/data/sample.txt")
    chunks = split_into_chunks(content)

    query_words = query.lower().split()

    best_chunk = ""
    max_matches = 0

    for chunk in chunks:
        chunk_lower = chunk.lower()
        match_count = 0

        for word in query_words:
            if word in chunk_lower:
                match_count += 1

        if match_count > max_matches:
            max_matches = match_count
            best_chunk = chunk

    if max_matches > 0:
        return f"Best match:\n{best_chunk.strip()}"

    return "No relevant information found."
    content = load_text("ai_project/data/sample.txt")
    chunks = split_into_chunks(content)

    query_words = query.lower().split()

    best_chunk = ""
    max_matches = 0

    for chunk in chunks:
        chunk_lower = chunk.lower()
        match_count = 0

        for word in query_words:
            if word in chunk_lower:
                match_count += 1

        if match_count > max_matches:
            max_matches = match_count
            best_chunk = chunk

    if max_matches > 0:
        return f"Best match:\n{chunk.strip()}"

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
