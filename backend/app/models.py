from sqlmodel import SQLModel, Field, Relationship


# Users

class User(SQLModel):
    pass




# Nutrients-Ingredients many-to-many

class NutrientIngredientLink(SQLModel, table=True):
    nutrient_id: int | None = Field(default=None, foreign_key="nutrient.id", primary_key=True)
    ingredient_id: int | None = Field(default=None, foreign_key="ingredient.id", primary_key=True)
    quantity: int

    nutrient: 'Nutrient' = Relationship(back_populates='ingredient_links')
    ingredient: 'Ingredient' = Relationship(back_populates='nutrient_links')




# Nutrients

class NutrientBase(SQLModel):
    name: str
    unit: str  # TODO add unit choices

    # def __add__(self, other):
    #     pass


class NutrientCreate(NutrientBase):
    pass


class NutrientUpdate(NutrientBase):
    pass


class Nutrient(NutrientBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    slug: str | None = Field(default=None, index=True, unique=True)

    ingredient_links: list[NutrientIngredientLink] = Relationship(back_populates='nutrient')


class NutrientPublic(NutrientBase):
    id: int




# Ingredients

class IngredientBase(SQLModel):
    name: str
    category: str  # TODO Add category choices
    rating: str  # TODO Add rating choices


class IngredientCreate(IngredientBase):
    pass


class IngredientUpdate(IngredientBase):
    pass


class Ingredient(IngredientBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    slug: str | None = Field(default=None, index=True, unique=True)

    nutrient_links: list[NutrientIngredientLink] = Relationship(back_populates='ingredient')


class IngredientPublic(IngredientBase):
    id: int




# Recipes

class RecipeBase(SQLModel):
    name: str
    # owner: User
    rating: str  # TODO Add rating choices


class RecipeCreate(RecipeBase):
    pass


class RecipeUpdate(RecipeBase):
    pass


class Recipe(RecipeBase, table=True):
    id: int | None = Field(default=None, primary_key=True)


class RecipePublic(RecipeBase):
    id: int




# Generic message

class Message(SQLModel):
    message: str




