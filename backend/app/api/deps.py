from collections.abc import Generator
from typing import Annotated, Type, TypeVar
from functools import partial

from fastapi import Depends
from sqlmodel import Session

from app.core.db import engine
from app.service import BaseService


ServiceType = TypeVar('ServiceType', bound=BaseService)


def get_db_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_db_session)]


def get_service(service_cls: Type[ServiceType], session: SessionDep) -> ServiceType:
    """
    Returns an instance of the service class initialized with the repository.
    """

    repository = service_cls.repository_cls(session)
    return service_cls(repository, session)


def service_dep(service_cls: Type[ServiceType]):
    return Depends(partial(get_service, service_cls))
