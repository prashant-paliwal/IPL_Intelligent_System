state = {
    "score": 0,
    "wickets": 0,
    "balls": 0
}

def update_context(e):
    state["score"] += e.get("runs", 0)
    state["balls"] += 1

    if e.get("event") == "wicket":
        state["wickets"] += 1

    return state