import sys
import os
sys.path.append(
    os.path.dirname(
        os.path.dirname(os.path.dirname(__file__))
    )
)

from app.tools.llm import get_embedding
from app.rag.store import store_memory
from app.rag.retrieve import retrieve_memory
from app.db.qdrant import init_qdrant

def test_rag():
    init_qdrant()
    
    # 🔹 Step 1: store memory
    text = "Kohli struggles against Bumrah in death overs"
    vec = get_embedding(text)

    store_memory(text, vec, id=1)

    print("✅ Stored")

    # 🔹 Step 2: query memory
    query = "Kohli vs Bumrah"
    q_vec = get_embedding(query)

    results = retrieve_memory(q_vec)

    print("🔍 Retrieved:", results)


if __name__ == "__main__":
    test_rag()