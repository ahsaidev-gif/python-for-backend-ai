from utils.file_loader import load_text, split_into_chunks, normalize_text
from utils.embedding_utils import generate_embedding, cosine_similarity
from utils.constants import stop_words


def retrieve_best_chunk(query):
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
    best_score = -1

    query_vec = generate_embedding(query)

    for chunk in chunks:
        chunk = normalize_text(chunk)

       # Keyword score
        chunk_words = set(chunk.split())
        keyword_score = len(query_words.intersection(chunk_words))

       # Embedding score
        chunk_vec = generate_embedding(chunk)
        embedding_score = cosine_similarity(query_vec, chunk_vec)

        # Combine both
        score = keyword_score + embedding_score

        if score > best_score:
            best_score = score
            best_chunk = chunk

    if best_score > 0:
        return best_chunk.strip()

    return None
