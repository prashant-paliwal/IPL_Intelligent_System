import textwrap
from app.tools.llm import call_llm
from app.agents.memory import run as memory_agent

async def run(state, features):
    memories = memory_agent(state, features)

    memory_text = "\n".join(memories) if memories else "No data"

    prompt = textwrap.dedent(f"""
        You are a cricket analyst.

        Match:
        Score: {state.score}/{state.wickets}
        Overs: {state.over}

        Features:
        Run Rate: {features['run_rate']}
        Momentum: {features['momentum']}
        Pressure: {features['pressure']}
        Phase: {features['phase']}

        Historical Context:
        {memory_text}

        Instructions:
        - Use memory if useful
        - Give 1 sharp insight
    """).strip()

    return await call_llm(prompt)