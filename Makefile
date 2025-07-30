dev:
	uv run uvicorn src.app.main:app --port 8080 --reload

init-venv:
	uv venv
	uv pip install -r requirements.txt

build:
	uv run src/build.py

view:
	uv run uvicorn src.view:app --port 8090