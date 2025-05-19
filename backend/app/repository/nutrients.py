from .base import BaseRepository

from app.models import Nutrient, NutrientCreate, NutrientUpdate


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
