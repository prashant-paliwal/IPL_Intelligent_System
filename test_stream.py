# test_stream.py
from app.stream.producer import publish

publish({
    "runs": 4,
    "batsman": "Kohli",
    "bowler": "Bumrah"
})