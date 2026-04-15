from langgraph.graph import StateGraph

from app.agents import commentary, analyst, hype
from app.agents.memory import run as memory_agent
from app.core.features import extract_features


# Define graph state
class GraphState(dict):
    pass


# --- Nodes ---

def state_node(state: GraphState):
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


# --- Build Graph ---

graph = StateGraph(GraphState)

graph.add_node("features", state_node)
graph.add_node("memory", memory_node)
graph.add_node("commentary", commentary_node)
graph.add_node("analyst", analyst_node)
graph.add_node("hype", hype_node)

graph.set_entry_point("features")

graph.add_edge("features", "memory")
graph.add_edge("memory", "commentary")
graph.add_edge("memory", "analyst")
graph.add_edge("memory", "hype")

graph.set_finish_point("hype")

app_graph = graph.compile()