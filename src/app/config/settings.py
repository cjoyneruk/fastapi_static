from pathlib import Path

APP_DIR = Path(__file__).resolve().parent.parent
SRC_DIR = APP_DIR.parent
ROOT_DIR = SRC_DIR.parent

# App settings
TEMPLATES_DIR = APP_DIR / 'templates'
STATIC_DIR = APP_DIR / 'static'

# Build settings
SITE_DIR = ROOT_DIR / 'site'
SITE_STATIC_DIR = SITE_DIR / 'static'
