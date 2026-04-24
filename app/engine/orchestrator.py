from app.db.qdrant import init_qdrant
from app.core.state import MatchState
from app.engine.graph import app_graph

init_qdrant()

state = MatchState()


async def process_event(event):
    state.update(event)
    result = await app_graph.invoke({
        "match_state": state
    })
    return result
