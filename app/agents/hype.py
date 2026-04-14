def run(state, features):
    if features["momentum"] > 10:
        return "🔥 Momentum shifting! Big over!"
    if features["pressure"] == "high":
        return "⚡ Pressure building! Wickets needed!"
    return "Game balanced."