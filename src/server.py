import code
import sys
from os import getenv

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from core import settings
from database.database import client


def get_application() -> FastAPI:
    """ get app with event handlers on and database loaded """
    app = FastAPI(
        debug=True, title=settings.PROJECT_NAME, version=settings.PROJECT_VERSION
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    client.start()
    client.migrate()
    client.generate_mapping()
    from app.routes import api

    app.include_router(api.router)

    return app


app = get_application()


if __name__ == "__main__":
    if "shell" in sys.argv:
        code.interact()
    else:
        uvicorn.run(
            "server:app",
            host="0.0.0.0",
            port=getenv("PORT", 8000),
            reload=True,
        )
