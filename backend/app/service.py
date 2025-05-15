from abc import ABC, abstractmethod
from typing import TypeVar, Generic, Type

from sqlmodel import Session

from app.repository import BaseRepository, NutrientRepository, Nutrient, NutrientCreate, NutrientUpdate
from app.exceptions import NutrientNotFound


RepositoryType = TypeVar('RepositoryType', bound=BaseRepository)


class BaseService(ABC, Generic[RepositoryType]):
    @property
    @abstractmethod
    def repository_cls(self) -> Type[RepositoryType]:
        pass

    def __init__(self, repository: RepositoryType, session: Session) -> None:
        self.repository = repository
        self.session = session


class NutrientService(BaseService[NutrientRepository]):
    repository_cls = NutrientRepository

    def create(self, nutrient_in: NutrientCreate) -> Nutrient:
        nutrient_db = self.repository.create(nutrient_in)

        self.session.commit()

        return nutrient_db
    
    def read(self) -> list[Nutrient]:
        return self.repository.read()

    def get(self, id: int) -> Nutrient:
        nutrient_db = self.repository.get(id)

        if not nutrient_db:
            raise NutrientNotFound()
        
        return nutrient_db
    
    def update(self, id: int, nutrient_in: NutrientUpdate) -> Nutrient:
        nutrient_db = self.repository.get(id)
        self.repository.update(nutrient_db, nutrient_in)

        self.session.commit()

        return nutrient_db
    
    def delete(self, id: int) -> None:
        nutrient_db = self.get(id)
        self.repository.delete(nutrient_db)

        self.session.commit()

        return None


        
