import dataclasses
import pathlib
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

db_path = pathlib.Path(__file__).parent.parent / "db/zuzu.db"

engine = create_engine(f"sqlite:///{db_path}")
session_maker = orm.sessionmaker(bind=engine)
table_mapper = orm.registry()


@dataclasses.dataclass
class TableConf:
    table = Table
    column = Column
    int_field = Integer
    str_field = String
    datetime_field = DateTime
    now = func.now

table_conf = TableConf()
