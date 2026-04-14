def match_phase(over):
    if over < 6:
        return "powerplay"
    elif over > 15:
        return "death"
    return "middle"

def extract_features(state):
    history = state.history

    total_runs = state.score
    overs = max(state.over, 1)

    run_rate = total_runs / overs

    last_5 = history[-5:]
    last_6 = history[-6:]

    momentum = sum(e.get("runs", 0) for e in last_6)
    boundaries = sum(1 for e in last_6 if e.get("runs") in [4, 6])

    phase = match_phase(state.over)

    if state.wickets >= 5 and run_rate < 7:
        pressure = "high"
    elif phase == "death" and run_rate < 8:
        pressure = "high"
    elif momentum >= 12:
        pressure = "low"
    elif run_rate < 6:
        pressure = "high"
    else:
        pressure = "medium"

    return {
        "run_rate": round(run_rate, 2),
        "momentum": momentum,
        "last_5": last_5,
        "boundaries_last_6": boundaries,
        "pressure": pressure,
        "phase": phase
    }