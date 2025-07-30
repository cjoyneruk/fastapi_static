from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from config import settings

app = FastAPI(title='Static generator')

templates = Jinja2Templates(settings.TEMPLATES_DIR)
app.mount("/static", StaticFiles(directory=settings.STATIC_DIR), name="static")

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