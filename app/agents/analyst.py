import textwrap
from app.tools.llm import call_llm

def run(state, features):
    prompt = textwrap.dedent(f"""
        You are a cricket analyst.

        Match Context:
        Score: {state.score}/{state.wickets}
        Overs: {state.over}

        Features:
        Run Rate: {features['run_rate']}
        Momentum: {features['momentum']}
        Pressure: {features['pressure']}
        Phase: {features['phase']}

        Instructions:
        - Give 1 short tactical insight
        - Be sharp and analytical
    """).strip()

    return call_llm(prompt)