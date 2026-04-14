from qdrant_client.models import PointStruct
from app.db.qdrant import client, COLLECTION


def store_memory(text: str, vector: list, id: int):
    client.upsert(
        collection_name=COLLECTION,
        points=[
            PointStruct(
                id=id,
                vector=vector,
                payload={"text": text}
            )
        ]
    )