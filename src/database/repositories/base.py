from re import match
from types import FunctionType
from typing import Any

from database.decorators import db_session


class __RepoDict(dict):
    def __setitem__(self, k: str, v: Any) -> None:
        if isinstance(v, FunctionType) and not match(r"^_", k):
            return super().__setitem__(k, db_session(v))
        return super().__setitem__(k, v)


class RepositoryMeta(type):
    @classmethod
    def __prepare__(cls, *args, **kwargs):
        return __RepoDict()

    def __new__(cls, name, bases, rp_dict):
        return super().__new__(cls, name, bases, dict(rp_dict))


class Repository(metaclass=RepositoryMeta):
    pass
