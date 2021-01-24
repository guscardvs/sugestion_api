from app.dtos.base import IdMixin, RWMixin


class EntryInDTO(RWMixin):
    user_id: str
    entry_id: str

class EntryDTO(EntryInDTO, IdMixin):
    pass

class SimpleResponseDTO(RWMixin):
    entry_id: str

class ListResponseDTO(RWMixin):
    entries: list[str]
