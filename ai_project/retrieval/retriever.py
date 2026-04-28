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

    results = []

    query_vec = generate_embedding(query)

    for chunk in chunks:
        chunk = normalize_text(chunk)

        # Keyword score
        chunk_words = {
            word for word in chunk.split()
            if word not in stop_words
        }

        keyword_score = len(query_words.intersection(chunk_words))

        # skip irrelevant chunks
        if keyword_score == 0:
            continue

        # Embedding score
        chunk_vec = generate_embedding(chunk)
        embedding_score = cosine_similarity(query_vec, chunk_vec)

        # Combine (improved)
        # Keyword = real signal
        # Embedding = fake (random)
        score = (5 * keyword_score) + embedding_score

        results.append((score, chunk))

        # sort by score (highest first)
    results.sort(reverse=True, key=lambda x: x[0])

    # take top 3
    top_chunks = [chunk for score, chunk in results[:3]]

    return top_chunks if top_chunks else None
