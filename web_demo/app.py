from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
import sys
import os

# Allow importing from Src
sys.path.append(os.path.abspath("../Src"))

from main import run_simulation

app = FastAPI()
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": ""})


@app.post("/", response_class=HTMLResponse)
async def simulate(request: Request, mode: str = Form(...), user_input: str = Form(...)):
    result = run_simulation(mode, user_input)
    return templates.TemplateResponse("index.html", {
        "request": request,
        "result": result
    })
