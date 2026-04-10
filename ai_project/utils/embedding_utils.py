import random


def generate_embedding(text):
    random.seed(hash(text))
    return [random.random() for _ in range(5)]


def cosine_similarity(vec1, vec2):
    return sum(a*b for a, b in zip(vec1, vec2))
