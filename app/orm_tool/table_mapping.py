import app.domain.models
from app.orm_tool import table_conf


zuz_table = table_conf.table(
    "zuzublik",
    app.orm_tool.table_mapper.metadata,
    table_conf.column("id", table_conf.int_field, primary_key=True, autoincrement=True),
    table_conf.column("title", table_conf.str_field(200), index=True, nullable=False),
    table_conf.column("url", table_conf.str_field(200), index=True, nullable=False),
    table_conf.column("xpath", table_conf.str_field(200), index=True, nullable=False),
    table_conf.column("creation_date", table_conf.datetime_field, server_default=table_conf.now(), nullable=False)
)


def start_mapping():
    app.orm_tool.table_mapper.map_imperatively(class_=app.domain.models.Zuzublik, local_table=zuz_table)
