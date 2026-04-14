from app.core.state import MatchState
from app.core.features import extract_features

from app.agents import commentary, analyst, hype

state = MatchState()


def process_event(event):
    state.update(event)

    features = extract_features(state)

    return {
        "commentary": commentary.run(state, features),
        "analysis": analyst.run(state, features),
        "hype": hype.run(state, features),
    }