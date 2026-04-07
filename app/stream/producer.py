import json
from app.db.redis import redis_client

def publish(event):
    redis_client.xadd("match_stream", {
        "data": json.dumps(event)
    })