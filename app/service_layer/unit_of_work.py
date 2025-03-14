from sqlalchemy.exc import IntegrityError

import app.domain.errors
from app.orm_tool import session_maker
from app.repository.repository import RepoProto, ZuzublikRepository


class UnitOfWork:
    def __init__(self):
        self.session_maker = session_maker

    def __enter__(self):
        self.session = self.session_maker()
        self.zuzu: RepoProto = ZuzublikRepository(session=self.session)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.rollback()
            self.session.close()
        self.session.close()

    def rollback(self):
        self.session.rollback()

    def commit(self):
        try:
            self.session.commit()
        except IntegrityError:
            raise app.domain.errors.AlreadyExistsError
