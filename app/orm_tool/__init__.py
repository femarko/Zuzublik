import dataclasses
from sqlalchemy import (
    create_engine,
    Table,
    Column,
    Integer,
    String,
    DateTime,
    func,
    orm
)

import app.config


engine = create_engine(app.config.config.get("database_url"))
session_maker = orm.sessionmaker(bind=engine)
table_mapper = orm.registry()

@dataclasses.dataclass
class TableConf:
    table = Table
    column = Column
    int_field = Integer
    str_field = String
    datetime_field = DateTime
    func_field = func

table_conf = TableConf()

