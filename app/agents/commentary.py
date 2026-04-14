import textwrap
from app.tools.llm import call_llm

def run(state, features):
    prompt = textwrap.dedent(f"""
        You are a professional IPL commentator.

        Match Situation:
        Score: {state.score}/{state.wickets}
        Overs: {state.over}
        Batsman: {state.striker}
        Last Ball: {state.last_ball}

        Context:
        Run Rate: {features['run_rate']}
        Momentum: {features['momentum']}
        Pressure: {features['pressure']}
        Phase: {features['phase']}

        Instructions:
        - Write 1 short exciting line
        - No explanation
        - Natural commentary style
    """).strip()

    return call_llm(prompt)