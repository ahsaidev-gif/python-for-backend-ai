from ai_project.utils.file_loader import load_text, split_into_chunks, normalize_text
from ai_project.utils.embedding_utils import generate_embedding, cosine_similarity
from ai_project.utils.constants import stop_words, SYNONYMS


def retrieve_best_chunk(query):
    if not query.strip():
        return None

    content = load_text("ai_project/data/knowledge_base.txt")
    chunks = split_into_chunks(content)

    query = normalize_text(query)

    query_words = set()

    for word in query.split():
        if word in stop_words:
            continue

        mapped = SYNONYMS.get(word, word)

        for w in mapped.split():
            query_words.add(w)

    best_chunk = ""
    best_score = -1

    query_vec = generate_embedding(query)

    for chunk in chunks:
        chunk = normalize_text(chunk)

        # Keyword score
        chunk_words = {
            word for word in chunk.split()
            if word not in stop_words
        }

        keyword_score = len(query_words.intersection(chunk_words))

        # Embedding score
        chunk_vec = generate_embedding(chunk)
        embedding_score = cosine_similarity(query_vec, chunk_vec)

        # Combine (improved)
        score = (2 * keyword_score) + embedding_score

        # FIXED BOOST
        if keyword_score > 0:
            score += 2

        if score > best_score:
            best_score = score
            best_chunk = chunk

    if best_score > 0:
        return best_chunk.strip()

    return None
