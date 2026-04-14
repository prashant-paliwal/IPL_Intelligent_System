import textwrap
from app.tools.llm import call_llm

def run(state, features):
    prompt = textwrap.dedent(f"""
        You are a hype IPL commentator.

        Context:
        Momentum: {features['momentum']}
        Pressure: {features['pressure']}

        Instructions:
        - Make it exciting / dramatic
        - 1 short line
    """).strip()

    return call_llm(prompt)