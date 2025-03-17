import dataclasses
import pathlib
from sqlalchemy.exc import IntegrityError
from sqlalchemy import (
    create_engine,
    Table,
    Column,
    Integer,
    String,
    DateTime,
    func,
    orm,
)
import app.config
import app.domain.models

db_path = pathlib.Path(__file__).parent.parent / "db/zuzu.db"

engine = create_engine(f"sqlite:///{db_path}")
session_maker = orm.sessionmaker(bind=engine)
table_mapper = orm.registry()


zuz_table = Table(
    "zuzublik",
    table_mapper.metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("title", String(200), index=True, nullable=False),
    Column("url", String(200), index=True, nullable=False),
    Column("xpath", String(200), index=True, nullable=False),
    Column("creation_date", DateTime, server_default=func.now(), nullable=False)
)


@dataclasses.dataclass
class ORMConf:
    integrity_error = IntegrityError
    engine = engine
    session_maker = session_maker

    @staticmethod
    def start_mapping():
        table_mapper.map_imperatively(class_=app.domain.models.Zuzublik, local_table=zuz_table)


orm_conf = ORMConf()
