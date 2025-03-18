import io
import pathlib
from pandas import read_excel


file_path = pathlib.Path(__file__).parent.parent.parent / "test_file.xls"

def parse_table(table_file):
    df = read_excel(io.BytesIO(table_file))
    result = df.to_dict(orient="records")
    return result
