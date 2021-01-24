from datetime import datetime

from database.database import Entity
from pony import orm


class User(Entity):
    id = orm.PrimaryKey(str)
    email = orm.Required(str, unique=True)
    first_name = orm.Optional(str)
    last_name = orm.Optional(str)
    password = orm.Required(str)
    created_at = orm.Required(datetime)
    last_login = orm.Optional(datetime)

    def before_insert(self):
        self.created_at = datetime.utcnow()
