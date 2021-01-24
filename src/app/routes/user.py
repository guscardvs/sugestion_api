from app.dtos.user import EditableUser, UserDTO, UserInDTO
from app.routes.base import CustomRouter
from database.repositories.user import UserRepository
from fastapi import Body, Path
from pydantic.types import UUID4

router = CustomRouter()

user_repository = UserRepository()


@router.create("/", response_model=UserDTO)
async def register_user(user_in: UserInDTO = Body(...)):
    return user_repository.register(user_in)


@router.get("/{id}", response_model=UserDTO)
async def get_user(id: UUID4 = Path(...)):
    return user_repository.get(id)


@router.put("/password/{id}")
async def change_password(id: UUID4 = Path(...), password: str = Body(..., embed=True)):
    return user_repository.change_password(id, password)


@router.put("/{id}", response_model=UserDTO)
async def edit_user(id: UUID4 = Path(...), edit_user: EditableUser = Body(...)):
    return user_repository.edit(id, edit_user)


@router.delete("/{id}", response_model=None)
async def delete_user(id: UUID4 = Path(...)):
    return user_repository.delete(id)
