import io
from pandas import read_excel

import app.domain.errors


def parse_table(table_file):
    try:
        df = read_excel(io.BytesIO(table_file))
    except ValueError:
        raise app.domain.errors.SmthWentWrong
    result = df.to_dict(orient="records")
    return result
