from .base import BaseService
from app.repository import NutrientRepository, Nutrient, NutrientCreate, NutrientUpdate
from app.exceptions import NutrientNotFound 


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