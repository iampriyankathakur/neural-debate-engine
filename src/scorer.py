from sklearn.metrics.pairwise import cosine_similarity
from src.embeddings import EmbeddingModel

embedder = EmbeddingModel()

def semantic_similarity_score(topic, argument):

    embeddings = embedder.encode([topic, argument])

    similarity = cosine_similarity(
        [embeddings[0]],
        [embeddings[1]]
    )[0][0]

    return float(similarity)
