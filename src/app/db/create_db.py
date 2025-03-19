import sqlite3
import pathlib

from src.app.orm_tool.sql_aclchemy_wrapper import orm_conf


db_path = pathlib.Path(__file__).parent / "zuzu.db"
connection = sqlite3.connect(f"{db_path}")
orm_conf.start_mapping()
orm_conf.create_tables()

