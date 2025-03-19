from typing import Any, Protocol

from src.app.domain import models


class NotFoundError(Exception):
    pass


class RepoProto(Protocol):
    def add(self, instance) -> None:
        pass

    def get(self, instance_id: int) -> Any:
        pass

    def delete(self, instance) -> None:
        pass


class Repository:
    def __init__(self, session):
        self.session = session
        self.model_cl = None

    def add(self, instance) -> None:
        self.session.add(instance)

    def get(self, instance_id: int) -> Any:
        return self.session.get(self.model_cl, instance_id)

    def delete(self, instance) -> None:
        self.session.delete(instance)


class ZuzublikRepository(Repository):
    def __init__(self, session):
        super().__init__(session=session)
        self.model_cl = models.Zuzublik
