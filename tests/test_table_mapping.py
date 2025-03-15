import sqlite3
import pathlib
import pytest

import app
from app.domain import models
from app.orm_tool import table_mapping, table_mapper, engine

@pytest.fixture(scope="session")
def do_mapping():
    app.orm_tool.table_mapping.start_mapping()


def test_start_mapping(do_mapping):
    assert next(iter(table_mapper.mappers)).class_ == models.Zuzublik


def test_create_table(do_mapping):
    db_path = pathlib.Path(__file__).parent.parent / "app/db/zuzu.db"
    table_mapper.metadata.create_all(engine)
    conn = sqlite3.connect(f"{db_path}")
    res = conn.execute("SELECT name FROM sqlite_master WHERE type='table' AND name LIKE 'zuzublik';")
    assert res.fetchall() == [('zuzublik',)]