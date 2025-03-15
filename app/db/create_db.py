import sqlite3
import pathlib


db_path = pathlib.Path(__file__).parent / "zuzu.db"
connection = sqlite3.connect(f"{db_path}")

