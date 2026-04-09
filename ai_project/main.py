"""
Basic CLI for AI assistant.
"""

from utils.file_loader import load_text, split_into_chunks, normalize_text
from llm_client import ask_llm

stop_words = {"is", "a", "the", "what", "in", "on", "at", "of", "for", "to"}


def get_user_query():
    return input("Ask your question: ")


def generate_response(query):
    content = load_text("ai_project/data/sample.txt")
    chunks = split_into_chunks(content)

    query = normalize_text(query)

    synonyms = {
        "ai": "artificial intelligence",
        "ml": "machine learning"
    }

    query_words = set()

    for word in query.split():
        if word in stop_words:
            continue

        mapped = synonyms.get(word, word)

        # split multi-word synonyms
        for w in mapped.split():
            query_words.add(w)

    best_chunk = ""
    best_score = 0

    for chunk in chunks:
        chunk = normalize_text(chunk)

        chunk_words = {
            word for word in chunk.split()
            if word not in stop_words
        }

        # find common words
        common_words = query_words.intersection(chunk_words)

        score = len(common_words)

        if score > best_score:
            best_score = score
            best_chunk = chunk

    if best_score > 0:
        return best_chunk.strip()

    return None


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
            chunk = generate_response(query)

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

            chunk = generate_response(query)

            if chunk:
                response = f"Best match:\n{chunk}"
            else:
                response = "No relevant information found."

        print("\nAnswer:")
        print(response)


if __name__ == "__main__":
    main()
