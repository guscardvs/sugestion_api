from datetime import datetime
from typing import Optional

from app.dtos.base import IdMixin, RWMixin
from pydantic.networks import EmailStr


class BaseUser(RWMixin):
    email: EmailStr
    first_name: Optional[str] = None
    last_name: Optional[str] = None


class UserInDTO(BaseUser):
    password: str


class UserDTO(BaseUser, IdMixin):
    created_at: datetime
    last_login: Optional[datetime] = None

class EditableUser(BaseUser):
    email: Optional[EmailStr] = None
