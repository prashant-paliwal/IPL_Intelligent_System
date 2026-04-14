# test_stream.py

from app.stream.producer import publish

events = [
    {"runs": 1, "batsman": "Kohli", "bowler": "Bumrah"},
    {"runs": 4, "batsman": "Kohli", "bowler": "Bumrah"},
    {"runs": 0, "batsman": "Kohli", "bowler": "Bumrah"},
    {"event": "wicket", "batsman": "Kohli", "bowler": "Bumrah"},
]

for e in events:
    publish(e)