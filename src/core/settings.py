from os import getenv
from pathlib import Path

BASE_DIR = Path(__file__).parent.parent

PROJECT_NAME = getenv("PROJECT_NAME", "FastAPI")

PROJECT_VERSION = getenv("PROJECT_VERSION", "0.0.1")

DATABASE = {
    "provider": "mysql",
    "user": "selfg",
    "password": "Chv5taffv$",
    "host": "localhost",
    "database": "solid",
    "port": 3306,
}

MIGRATIONS = BASE_DIR / "database" / "migrations"
