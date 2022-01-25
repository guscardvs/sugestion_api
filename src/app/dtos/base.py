from datetime import datetime
from re import sub
from typing import Optional
from uuid import uuid4

from pydantic import BaseModel
from pydantic.class_validators import validator
from pydantic.types import UUID4


class IdMixin(BaseModel):
    id: str

    @validator("id", always=True, pre=True)
    def validate_id(cls, value):
        return value or str(uuid4())

class RWMixin(BaseModel):
    class Config:
        allow_population_by_field_name = True

        @classmethod
        def alias_generator(cls, string: str) -> str:
            return sub("_([a-zA-Z])", lambda match: match[1].upper(), string)
