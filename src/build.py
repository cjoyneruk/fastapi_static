from .app.main import app, STATIC_DIR
from fastapi.routing import APIRoute
from fastapi.testclient import TestClient
from pathlib import Path
import os
import shutil

SRC_DIR = Path(__file__).resolve().parent
ROOT_DIR = SRC_DIR.parent
SITE_DIR = ROOT_DIR / 'site'
SITE_STATIC_DIR = SITE_DIR / 'static'

if __name__ == '__main__':

    with TestClient(app=app) as client:

        for r in app.routes:
                
            if isinstance(r, APIRoute):
                
                url = r.path

                response = client.get(url=url)

                html = response.text

                local_path = SITE_DIR / url.strip('/') / 'index.html'
                
                os.makedirs(local_path.parent, exist_ok=True)
                
                print(f'Rendering route {r.name} to {local_path}')

                with open(local_path, 'w') as f:
                    f.write(html)

    print('Copying static files')

    if SITE_STATIC_DIR.exists():
        shutil.rmtree(SITE_STATIC_DIR)

    shutil.copytree(STATIC_DIR, SITE_STATIC_DIR)