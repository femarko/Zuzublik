import io
from pandas import read_excel


def parse_table(table_file):
    df = read_excel(io.BytesIO(table_file))
    result = df.to_dict(orient="records")
    return result
