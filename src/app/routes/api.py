from app.routes import entry
from fastapi import APIRouter

router = APIRouter()

router.include_router(entry.router, prefix="/entry", tags=["Entry"])
