def run(state, features):
    return (
        f"{state.striker} scores {state.last_ball.get('runs', 0)}. "
        f"Score: {state.score}/{state.wickets} in {state.over} overs."
    )