import sqlite3
import pathlib
import pytest

import app
import app.orm_tool
from app.domain import models
from app.orm_tool import sql_aclchemy_wrapper
from app.orm_tool.sql_aclchemy_wrapper import engine, table_mapper


@pytest.fixture(scope="session")
def do_mapping():
    app.orm_tool.sql_aclchemy_wrapper.orm_conf.start_mapping()


def test_start_mapping(do_mapping):
    assert next(iter(table_mapper.mappers)).class_ == models.Zuzublik


def test_create_table(do_mapping):
    db_path = pathlib.Path(__file__).parent.parent / "app/db/zuzu.db"
    table_mapper.metadata.create_all(engine)
    conn = sqlite3.connect(f"{db_path}")
    res = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'zuzublik';").fetchall()
    conn.close()
    assert res == [('zuzublik',)]
