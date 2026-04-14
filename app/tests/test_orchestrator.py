import sys
import os
sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.dirname(__file__))
    )
)

from app.engine.orchestrator import process_event

events = [
    {"runs": 4, "batsman": "Kohli"},
    {"runs": 6, "batsman": "Kohli"},
    {"runs": 1, "batsman": "Kohli"},
]

for e in events:
    print(process_event(e))