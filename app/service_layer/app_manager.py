from app.domain import models
from app.auxiliary_services.parser import parse_table


def add_zuzublik(file, parser, validator, uow) -> int:
    parsed_data = parser(file)
    validated_data = validator(**parsed_data)
    with uow:
        for item in validated_data:
            zuz_instance = models.create_zuzublik(**item)
            uow.zuzublik_repo.add(zuz_instance)
        uow.commit()
    zuz_instance_id: int = zuz_instance.id
    return zuz_instance_id
