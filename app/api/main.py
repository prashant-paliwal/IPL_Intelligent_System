from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from app.engine.orchestrator import process_event
import os

app = FastAPI()



app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(
    directory=os.path.join(os.path.dirname(__file__), "../templates")
)

@app.get("/")
async def home():
    return {"status": "ok"}

@app.get("/index")
async def index(request: Request):
    print("Home Hit")
    return templates.TemplateResponse(
        name="index.html",
        request=request
    )


@app.post("/event")
async def handle_event(event: dict):
    return await process_event(event)