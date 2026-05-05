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

    return {
        # --- AI outputs (from graph) ---
        "commentary": result.get("commentary"),
        "analysis": result.get("analysis"),
        "hype": result.get("hype"),
        "prediction": result.get("prediction"),
        "features": result.get("features"),

        # --- REAL STATE (critical) ---
        "state": {
            "score": state.score,
            "wickets": state.wickets,
            "over": state.over,
            "striker": state.striker,
            "bowler": state.bowler
        }
    }