from langgraph.graph import StateGraph

from app.agents import commentary, analyst, hype, predictor
from app.agents.memory import run as memory_agent
from app.core.features import extract_features

from typing import TypedDict

class GraphState(TypedDict, total=False):
    match_state: dict
    features: dict
    memory: list
    commentary: str
    analysis: str
    hype: str
    prediction: dict

# --- Nodes ---

def features_node(state: dict):
    return {
        "match_state": state["match_state"],
        "features": extract_features(state["match_state"])
    }


def memory_node(state: dict):
    return {
        "match_state": state["match_state"],   # keep state alive
        "features": state["features"],         # keep features
        "memory": memory_agent(
            state["match_state"],
            state["features"]
        )
    }


async def commentary_node(state: dict):
    return {
        "commentary": await commentary.run(
            state["match_state"],
            state["features"]
        )
    }


async def analyst_node(state: dict):
    return {
        "analysis": await analyst.run(
            state["match_state"],
            state["features"]
        )
    }


async def hype_node(state: dict):
    return {
        "hype": await hype.run(
            state["match_state"],
            state["features"]
        )
    }


def predictor_node(state: dict):
    return {
        "prediction": predictor.run(
            state["match_state"],
            state["features"]
        )
    }


# --- Build Graph ---

graph = StateGraph(GraphState)

# Nodes
graph.add_node("features", features_node)
graph.add_node("memory", memory_node)
graph.add_node("commentary", commentary_node)
graph.add_node("analyst", analyst_node)
graph.add_node("hype", hype_node)
graph.add_node("predictor", predictor_node)

# Entry
graph.set_entry_point("features")

# Flow
graph.add_edge("features", "memory")

# Parallel fan-out
graph.add_edge("memory", "commentary")
graph.add_edge("memory", "analyst")
graph.add_edge("memory", "hype")
graph.add_edge("memory", "predictor")

# Finish
graph.set_finish_point("predictor")

# Compile
app_graph = graph.compile()