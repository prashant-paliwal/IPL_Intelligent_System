from app.db.qdrant import client, COLLECTION


def retrieve_memory(vector: list):
    results = client.query_points(
        collection_name=COLLECTION,
        query=vector,
        limit=3
    )

    return [r.payload["text"] for r in results.points]