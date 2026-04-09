"""
Basic CLI for AI assistant.
"""

from utils.file_loader import load_text, split_into_chunks
from llm_client import ask_llm

stop_words = {"is", "a", "the", "what", "in", "on", "at", "of", "for", "to"}


def get_user_query():
    return input("Ask your question: ")


def generate_response(query):
    content = load_text("ai_project/data/sample.txt")
    chunks = split_into_chunks(content)

    query_words = {
        word for word in query.lower().split()
        if word not in stop_words
    }

    best_chunk = ""
    best_score = 0

    for chunk in chunks:
        chunk_words = {
            word for word in chunk.lower().split()
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
            #  Try LLM first
            # response = ask_llm(query)

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

            # fallback to your logic
            chunk = generate_response(query)

            if chunk:
                response = f"Best match:\n{chunk}"
            else:
                response = "No relevant information found."

        print("\nAnswer:")
        print(response)


if __name__ == "__main__":
    main()
