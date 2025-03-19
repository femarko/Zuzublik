import pydantic
from typing import TypeVar, Type, Optional

import src.app.domain.errors


PydanticModel = TypeVar("PydanticModel", bound=pydantic.BaseModel)


class AddZuzublik(pydantic.BaseModel):
    title: Optional[str] = None
    url: Optional[str] = None
    xpath: Optional[str] = None


def validate_data(validation_model: Type[PydanticModel], data: dict[str, str]) -> dict[str, str]:
    try:
        return validation_model.model_validate(data).model_dump(exclude_unset=True)
    except pydantic.ValidationError as e:
        errors_list = e.errors()
        for item in errors_list:
            del item["url"]
        raise src.app.domain.errors.ValidationError(errors_list)


def validate_zuzublik_data(zuzublik_data: list[dict[str, str]]) -> list[dict[str, str]]:
    return [validate_data(validation_model=AddZuzublik, data={**item}) for item in zuzublik_data]