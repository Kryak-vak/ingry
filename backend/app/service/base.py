from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Type

from sqlmodel import Session

from app.repository import BaseRepository


RepositoryType = TypeVar('RepositoryType', bound=BaseRepository)


class BaseService(ABC, Generic[RepositoryType]):
    @property
    @abstractmethod
    def repository_cls(self) -> Type[RepositoryType]:
        pass

    def __init__(self, repository: RepositoryType, session: Session) -> None:
        self.repository = repository
        self.session = session
