from uuid import UUID

from app.dtos.entry import EntryDTO, EntryInDTO
from database.decorators import db_session
from database.entities.entry import Entry
from database.repositories.base import Repository
from pony.orm import count
from pony.orm.core import desc, select


class EntryRepository(Repository):
    def set_entry(self, entry_in: EntryInDTO):
        entry_dto = EntryDTO.parse_obj({**entry_in.dict(), "id": None})
        entry = Entry(**entry_dto.dict())
        return entry_dto

    def get_entry(self, entry_id: UUID):
        entry = Entry.get(id=str(entry_id))
        return EntryDTO.parse_obj(entry.to_dict())

    def _order_entry_by_popularity(self, user_id: str):
        return select(
            (e.entry_id, count(e)) for e in Entry if e.user_id == user_id
        ).order_by(lambda e_id, cte: desc(cte))

    def get_most_suggested(self, user_id: str) -> str:
        return self._order_entry_by_popularity(user_id)[:][0][0]

    def get_top_suggestions(self, user_id: str) -> list[str]:
        entry_ids = self._order_entry_by_popularity(user_id)[:5]
        return [item for item, _ in entry_ids]
