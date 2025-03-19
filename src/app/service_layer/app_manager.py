from src.app.domain import models


def add_zuzublik(file, parser, validator, uow) -> tuple[list[int], list[dict[str, str]]]:
    parsed_data = parser(file)
    validated_data = validator(parsed_data)
    with uow:
        id_list = []
        for item in validated_data:
            zuz_instance = models.create_zuzublik(**item)
            uow.zuzublik_repo.add(zuz_instance)
            uow.commit()
            id_list.append(zuz_instance.id)
    return id_list, validated_data
