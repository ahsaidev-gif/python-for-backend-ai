from openai import OpenAI

client = OpenAI()

# ADD CACHE
embedding_cache = {}


def generate_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding


# FUNCTION
def get_embedding(text):
    if text not in embedding_cache:
        embedding_cache[text] = generate_embedding(text)
    return embedding_cache[text]


def cosine_similarity(vec1, vec2):
    return sum(a * b for a, b in zip(vec1, vec2))
