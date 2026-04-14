
def generate_commentary(e):
    runs = e.get("runs", 0)

    if e.get("event") == "wicket":
        return f"OUT! {e['batsman']} is gone! Big breakthrough by {e['bowler']}!"

    if runs == 6:
        return f"SIX! {e['batsman']} launches it into the stands!"

    if runs == 4:
        return f"FOUR! Cracking shot by {e['batsman']}!"

    if runs == 0:
        return f"Dot ball. Good delivery by {e['bowler']}."

    return f"{runs} run{'s' if runs > 1 else ''} taken."