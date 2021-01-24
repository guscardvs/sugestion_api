from functools import wraps
from typing import TypeVar

from pony import orm

Callable_T = TypeVar("Callable_T")

def db_session(func: Callable_T) -> Callable_T:
    @wraps(func)
    def __db_session(*args, **kwargs):
        return orm.db_session(func)(*args, **kwargs)
    return __db_session
