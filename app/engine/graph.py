from langgraph.graph import StateGraph

from app.agents import commentary, analyst, hype, predictor
from app.agents.memory import run as memory_agent
from app.core.features import extract_features


class GraphState(dict):
    pass


# --- Nodes ---

def features_node(state: GraphState):
    state["features"] = extract_features(state["match_state"])
    return state


def memory_node(state: GraphState):
    state["memory"] = memory_agent(state["match_state"], state["features"])
    return state


def commentary_node(state: GraphState):
    state["commentary"] = commentary.run(state["match_state"], state["features"])
    return state


def analyst_node(state: GraphState):
    state["analysis"] = analyst.run(state["match_state"], state["features"])
    return state


def hype_node(state: GraphState):
    state["hype"] = hype.run(state["match_state"], state["features"])
    return state


def predictor_node(state: GraphState):
    state["prediction"] = predictor.run(
        state["match_state"],
        state["features"]
    )
    return state


# --- Build Graph ---

graph = StateGraph(GraphState)

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

# Fan-out (parallel-ready)
graph.add_edge("memory", "commentary")
graph.add_edge("memory", "analyst")
graph.add_edge("memory", "hype")
graph.add_edge("memory", "predictor")


# Finish → AFTER all nodes
graph.set_finish_point("predictor")

app_graph = graph.compile()