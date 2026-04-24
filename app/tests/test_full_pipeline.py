import sys
import os
sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.dirname(__file__))
    )
)

import asyncio
from app.engine.orchestrator import process_event

async def test_pipeline():
    events = [
        {"runs": 4, "batsman": "Kohli", "bowler": "Bumrah"},
        {"runs": 6, "batsman": "Kohli", "bowler": "Bumrah"},
        {"runs": 0, "batsman": "Kohli", "bowler": "Bumrah"},
    ]

    for e in events:
        result = await process_event(e)   # await here
        print("\n🔥 RESULT:\n", result)


if __name__ == "__main__":
    asyncio.run(test_pipeline())