import io
import pathlib
from typing import Iterable, Optional
from pandas import read_excel


file_path = pathlib.Path(__file__).parent.parent.parent / "test_file.xls"

def parse_table(table_file, fields: Optional[Iterable] = None):
    df = read_excel(io.BytesIO(table_file))
    # result: dict[str, str] = {}
    if fields is not None:
        columns = fields
    result = df.to_dict(orient="records")
    # for row_index in range(len(df)):
    #     for column in df.columns:
    #         result |= {column: df[column][row_index]}
    return result
