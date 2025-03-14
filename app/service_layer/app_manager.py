from app.domain import models
from app.side_services.parser import parse_table


def add_zuzublik(file, parser, validator, uow) -> int:
    parsed_data = parser(file)
    validated_data = validator(**parsed_data)
    zuz_instance = models.create_zuzublik(**validated_data)
    with uow:
        uow.zuzublik_repo.add(zuz_instance)
        uow.commit()
        zuz_instance_id: int = zuz_instance.id
    return zuz_instance_id
