def run(state, features):
    """
    Hybrid prediction:
    - rule-based (fast)
    - later upgrade → ML / LLM
    """

    # Basic win probability logic
    score = state.score
    wickets = state.wickets
    over = state.over
    run_rate = features["run_rate"]

    # simple heuristic
    if over < 10:
        base = 0.5
    elif over < 16:
        base = 0.6
    else:
        base = 0.7

    # adjust based on wickets
    if wickets > 5:
        base -= 0.2

    # adjust based on run rate
    if run_rate > 8:
        base += 0.1
    elif run_rate < 6:
        base -= 0.1

    win_prob = max(0.05, min(0.95, base))

    # 🔥 Next ball prediction (simple)
    if features["momentum"] > 10:
        next_ball = "boundary likely"
    elif features["pressure"] == "high":
        next_ball = "wicket chance"
    else:
        next_ball = "dot or single"

    return {
        "win_probability": round(win_prob, 2),
        "next_ball": next_ball
    }