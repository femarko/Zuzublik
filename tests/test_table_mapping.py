import sqlite3
import pathlib
import pytest

from src.app.domain import models
# from src.app import engine, table_mapper
from src.app.orm_tool.sql_aclchemy_wrapper import orm_conf, table_mapper

@pytest.fixture(scope="session")
def do_mapping():
    orm_conf.start_mapping()


def test_start_mapping(do_mapping):
    assert next(iter(table_mapper.mappers)).class_ == models.Zuzublik


def test_create_table(do_mapping):
    db_path = pathlib.Path(__file__).parents[1] / "src/app/db/zuzu.db"
    table_mapper.metadata.create_all(orm_conf.engine)
    conn = sqlite3.connect(f"{db_path}")
    res = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'zuzublik';").fetchall()
    conn.close()
    assert res == [('zuzublik',)]
