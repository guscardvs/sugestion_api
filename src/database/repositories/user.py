from app.dtos.user import EditableUser, UserDTO, UserInDTO
from database.entities.user import User
from database.repositories.base import Repository
from fastapi import HTTPException
from passlib.context import CryptContext
from pydantic.types import UUID4


class UserRepository(Repository):
    def __init__(self):
        self.ctx = CryptContext(schemes=["bcrypt"])

    def register(self, user_in: UserInDTO):
        if User.get(email=user_in.email):
            raise HTTPException(409, detail="Email already used")
        user = UserDTO.parse_obj(user_in.dict())
        User(**{**user.dict(), "password": self.ctx.hash(user_in.password)})
        return user

    def get_db(self, id: UUID4) -> User:
        db_user = User.get(id=id)
        if db_user:
            return db_user
        raise HTTPException(404, detail="User not found")

    def get(self, id: UUID4):
        return UserDTO.parse_obj(self.get_db_user(id).to_dict())

    def edit(self, id: UUID4, edit_user: EditableUser):
        user = self.get_db(id)
        user.set(**{key: value for key, value in edit_user.dict().items() if value})
        return UserDTO.parse_obj(user.to_dict())

    def change_password(self, id: UUID4, new_password):
        user = self.get_db(id)
        user.password = self.ctx.hash(new_password)

    def verify_password(self, id: UUID4, password: str) -> bool:
        user = self.get_db(id)
        return self.ctx.verify(password, user.password)

    def delete(self, id: UUID4):
        self.get_db_user(id).delete()
