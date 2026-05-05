# 🏏 IPL Intelligent AI System

## 🚀 Overview

An autonomous, real-time cricket intelligence system built using multi-agent AI.
It simulates live IPL matches and generates:

* 🎙 AI Commentary (human-like)
* 📊 Match Analysis (context-aware)
* 🔥 Hype Narratives (engagement layer)
* 📈 Win Predictions (dynamic)
* 🧠 Memory-based Insights (RAG)

Designed as a **production-grade, stateful AI system**, not a demo.

---

## 🧠 System Architecture

```
Frontend (FastAPI + Jinja UI)
        ↓
API Layer (process_event)
        ↓
LangGraph Orchestrator
        ↓
Multi-Agent System
    ├── Commentary Agent
    ├── Analyst Agent
    ├── Hype Agent
    ├── Predictor Agent
    └── Memory Agent (RAG)
        ↓
State Engine (MatchState)
        ↓
Vector DB (Qdrant)
```

---

## ⚙️ Core Concepts

### 1. Stateful Engine

The system maintains a live match state:

```python
MatchState:
- score
- wickets
- overs
- striker / bowler
```

This ensures:

* consistency across events
* realistic simulation
* proper feature extraction

---

### 2. Multi-Agent AI (LangGraph)

Each event triggers multiple agents:

| Agent      | Responsibility                  |
| ---------- | ------------------------------- |
| Commentary | Generate ball-by-ball narration |
| Analyst    | Provide deep insights           |
| Hype       | Add excitement layer            |
| Predictor  | Estimate match outcome          |
| Memory     | Retrieve historical context     |

---

### 3. RAG (Retrieval-Augmented Generation)

* Uses **Qdrant vector DB**
* Stores past cricket knowledge
* Retrieves context like:

  * "Kohli struggles vs Bumrah in death overs"

---

### 4. Real-Time Pipeline

```
Ball Event → State Update → Graph Execution → AI Output → UI Update
```

---

## 🖥️ UI Features

* Clean white dashboard (Cricbuzz-style)
* Live scoreboard (no hardcoding)
* Run rate, pressure, win %
* Streaming commentary updates
* Smooth animation transitions

---

## 🔁 Live Simulation

* Auto match simulation (no manual input)
* Backend-driven state
* UI reflects real-time AI output

---

## 📦 Tech Stack

### Backend

* FastAPI
* LangGraph
* LiteLLM
* Qdrant (Vector DB)

### Frontend

* Jinja2 Templates
* Vanilla JS (no React)
* CSS (CSP-safe, modular)

### Infra

* Async Python
* Event-driven architecture

---

## ▶️ Running the Project

### 1. Setup

```bash
python -m venv .venv
.venv\Scripts\activate   # Windows
```

### 2. Install

```bash
pip install -r requirements.txt
```

OR (uv users):

```bash
python -m uv sync
```

---

### 3. Run Server

```bash
python -m uvicorn app.api.main:app --reload
```

---

### 4. Open UI

```
http://127.0.0.1:8000/index
```

---

## 📡 API Example

### POST `/event`

```json
{
  "runs": 4,
  "batsman": "Kohli",
  "bowler": "Bumrah"
}
```

---

### Response

```json
{
  "commentary": "...",
  "analysis": "...",
  "hype": "...",
  "prediction": {
    "win_probability": 0.6,
    "next_ball": "dot or single"
  },
  "features": {
    "run_rate": 8.2,
    "pressure": "medium"
  },
  "state": {
    "score": 32,
    "wickets": 1,
    "over": 4.2
  }
}
```

---

## 🔥 Key Highlights

* ✅ Multi-agent AI system (not single prompt)
* ✅ Fully async + scalable pipeline
* ✅ RAG integration (memory-aware AI)
* ✅ Real-time UI (state-driven)
* ✅ Production-style architecture
* ✅ No frontend framework dependency

---

## 🧩 Future Improvements

* WebSocket streaming (true real-time)
* Advanced prediction models (ML-based)
* Player-specific embeddings
* Voice commentary (TTS)
* Live match ingestion (real IPL feeds)

---

## 💡 Why This Project Matters

Most AI projects are:

```
Prompt → Response → Done
```

This system is:

```
State → Multi-Agent → Memory → Prediction → UI
```

👉 That’s **real AI system design**

---

## 👨‍💻 Author

Prashant Paliwal
Software Developer

---

## ⭐ Final Note

This project demonstrates:

* System design thinking
* AI orchestration (LangGraph)
* Real-time pipelines
* Production mindset
