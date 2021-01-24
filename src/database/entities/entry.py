from database.database import Entity
from pony import orm


class Entry(Entity):
    id = orm.PrimaryKey(str)
    user_id = orm.Required(str)
    entry_id = orm.Required(str)
    
