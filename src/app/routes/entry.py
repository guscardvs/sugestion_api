from app.dtos.entry import (EntryDTO, EntryInDTO, ListResponseDTO,
                            SimpleResponseDTO)
from app.routes.base import CustomRouter
from database.repositories.entry import EntryRepository
from fastapi import Body, Path
from pydantic.types import UUID4

router = CustomRouter()

entry_repository = EntryRepository()


@router.create("/", response_model=EntryDTO)
async def create_entry(entry_in: EntryInDTO = Body(...)):
    return entry_repository.set_entry(entry_in)


@router.get("/id/{id}", response_model=EntryDTO)
async def get_entry_by_id(id: UUID4 = Path(...)):
    return entry_repository.get_entry(id)


@router.get("/first/{user_id}", response_model=SimpleResponseDTO)
async def get_most_suggested_entry(user_id: str):
    return SimpleResponseDTO(entry_id=entry_repository.get_most_suggested(user_id))


@router.get("/top/{user_id}", response_model=ListResponseDTO)
async def get_top_five_entries(user_id: str):
    return ListResponseDTO(entries=entry_repository.get_top_suggestions(user_id))
