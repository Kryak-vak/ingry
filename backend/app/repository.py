
from abc import ABC, abstractmethod
from typing import Any, TypeVar, Generic

from sqlmodel import Session, SQLModel, select

from app.models import Nutrient, NutrientCreate, NutrientUpdate


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


class NutrientRepository(BaseRepository[Nutrient]):
    model = Nutrient

    def create(self, model_in: NutrientCreate) -> Nutrient:
        nutrient_db = self.model.model_validate(model_in)
        self.session.add(nutrient_db)

        return nutrient_db

    def update(self, model_db: Nutrient, model_in: NutrientUpdate) -> Nutrient:
        model_in_dict = model_in.model_dump(exclude_unset=True)
        model_db.sqlmodel_update(model_in_dict)
        self.session.add(model_db)
        
        return model_db
    
    def delete(self, model_db: Nutrient) -> None:
        self.session.delete(model_db)
        
        return None

    
