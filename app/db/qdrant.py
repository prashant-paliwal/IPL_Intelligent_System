from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

client = QdrantClient(":memory:")

COLLECTION = "cricket_memory"

def init_qdrant():
    """
    Initialize collection safely (no overwrite)
    """
    if not client.collection_exists(COLLECTION):
        client.create_collection(
            collection_name=COLLECTION,
            vectors_config=VectorParams(
                size=1536,  # OpenAI embedding size
                distance=Distance.COSINE
            )
        )