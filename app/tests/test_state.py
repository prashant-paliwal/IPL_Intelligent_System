import sys
import os
sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.dirname(__file__))
    )
)

from app.core.state import MatchState
from app.core.features import extract_features


def test_state():
    state = MatchState()

    events = [
         {"runs": 1}, {"runs": 4}, {"runs": 2},
        {"runs": 6}, {"runs": 0}, {"runs": 3}
    ]

    for e in events:
        state.update(e)

    features = extract_features(state)

    print(state.snapshot())
    print(features)

    print(features["phase"], features["pressure"])



if __name__ == "__main__":
    test_state()