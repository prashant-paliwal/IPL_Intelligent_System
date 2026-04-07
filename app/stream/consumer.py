import json
from app.db.redis import redis_client

async def consume():
    last_id = "0"

    while True:
        events = redis_client.xread(
            {"match_stream": last_id},
            block=0
        )

        for _, msgs in events:
            for msg_id, data in msgs:
                event = json.loads(data["data"])
                print("EVENT:", event)
                last_id = msg_id