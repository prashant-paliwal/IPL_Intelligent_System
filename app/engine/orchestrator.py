from app.core.state import MatchState
from app.engine.graph import app_graph

state = MatchState()


def process_event(event):
    state.update(event)
    result = app_graph.invoke({
        "match_state": state
    })
    return result
