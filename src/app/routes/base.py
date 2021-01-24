from typing import Any, Callable, Optional, Sequence

from fastapi import APIRouter, params
from fastapi.types import DecoratedCallable
from starlette.status import HTTP_201_CREATED


class CustomRouter(APIRouter):
    def create(
        self,
        path: str,
        *,
        response_model: Optional[type[Any]],
        dependencies: Optional[Sequence[params.Depends]] = None,
        summary: Optional[str] = None,
        description: Optional[str] = None
    ) -> Callable[[DecoratedCallable], DecoratedCallable]:
        return super().post(
            path,
            response_model=response_model,
            status_code=HTTP_201_CREATED,
            dependencies=dependencies,
            summary=summary,
            description=description,
        )
