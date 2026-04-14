from app.tools.llm import get_embedding
from app.rag.retrieve import retrieve_memory

def run(state, features):
    query = f"{state.striker} vs {state.bowler}"

    vector = get_embedding(query)

    memories = retrieve_memory(vector)

    return memories