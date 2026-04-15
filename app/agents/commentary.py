import textwrap
from app.tools.llm import call_llm
from app.agents.memory import run as memory_agent

def run(state, features):
    memories = memory_agent(state, features)
    
    memory_text = "\n".join(memories) if memories else "No historical insights"

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

        Historical Insights:
        {memory_text}

        Instructions:
        - Use historical insights if relevant
        - Keep it short (1 line)
        - Sound natural and exciting
    """).strip()

    return call_llm(prompt)