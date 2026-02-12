from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

# Src को import path में add करो (root से relative)
import sys
import os

# Root directory से Src को add (क्योंकि app.py root में है)
sys.path.append(os.path.abspath("Src"))
# या अगर AI core में main.py है: sys.path.append(os.path.abspath("Src/AI core"))

from main import run_simulation   # अब ये काम करेगा अगर Src में main.py है
# अगर Src/AI core/main.py है तो: from AI_core.main import run_simulation

app = FastAPI(title="NetraAI Simulation")
templates = Jinja2Templates(directory="templates")  # root में templates/ फोल्डर


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "result": ""}
    )


@app.post("/", response_class=HTMLResponse)
async def simulate(
    request: Request,
    mode: str = Form(...),
    user_input: str = Form(...)
):
    try:
        result = run_simulation(mode, user_input)
    except Exception as e:
        result = f"Error: {str(e)}"  # बेहतर error handling

    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "result": result
        }
    )


# Optional: run locally के लिए (uvicorn app:app --reload)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
