from abc import ABC, abstractmethod
from typing import Any, TypeVar, Generic

from sqlmodel import Session, SQLModel, select


ModelType = TypeVar('ModelType', bound=SQLModel)


class BaseRepository(ABC, Generic[ModelType]):
    model: type[ModelType]

    def __init__(self, session: Session) -> None:
        self.session = session

    @abstractmethod
    def create(self, model_in: ModelType) -> ModelType:
        pass

    def read(self) -> list[ModelType]:
        return self.session.exec(select(self.model)).all()

    def get(self, id: int) -> ModelType | None:
        return self.session.get(self.model, id)
    
    @abstractmethod
    def update(self, model_db: ModelType, model_in: ModelType) -> ModelType:
        pass
    
    @abstractmethod
    def delete(self, model_db: ModelType) -> None:
        pass
    
