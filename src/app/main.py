from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent
TEMPLATES_DIR = APP_DIR / 'templates'
STATIC_DIR = APP_DIR / 'static'

app = FastAPI(title='Static generator')

templates = Jinja2Templates(TEMPLATES_DIR)
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

@app.get('/', name='home')
def home(request: Request) -> HTMLResponse:

    return templates.TemplateResponse(
        request=request,
        name='pages/index.html'
    )

@app.get('/about', name='about')
def about(request: Request) -> HTMLResponse:

    return templates.TemplateResponse(
        request=request,
        name='pages/about.html'
    )


routes = app.routes