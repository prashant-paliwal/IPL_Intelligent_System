# app/engine/insight.py

def generate_insight(ctx):
    overs = ctx["balls"] / 6
    run_rate = ctx["score"] / overs if overs > 0 else 0

    return f"Score: {ctx['score']}/{ctx['wickets']} | RR: {run_rate:.2f}"