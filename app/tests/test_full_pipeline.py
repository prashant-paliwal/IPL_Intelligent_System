import sys
import os
sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.dirname(__file__))
    )
)
from app.engine.orchestrator import process_event

def test_pipeline():
    events = [
        {"runs": 4, "batsman": "Kohli", "bowler": "Bumrah"},
        {"runs": 6, "batsman": "Kohli", "bowler": "Bumrah"},
        {"runs": 0, "batsman": "Kohli", "bowler": "Bumrah"},
    ]

    for e in events:
        result = process_event(e)
        print("\n RESULT:\n", result)


if __name__ == "__main__":
    test_pipeline()