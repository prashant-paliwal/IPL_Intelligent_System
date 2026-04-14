def run(state, features):
    return (
        f"Run rate: {features['run_rate']}, "
        f"Momentum: {features['momentum']}, "
        f"Pressure: {features['pressure']}"
    )