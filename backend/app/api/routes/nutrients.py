from fastapi import APIRouter, Depends

from app.api.deps import service_dep
from app.service import NutrientService
from app.models import Nutrient, NutrientPublic, NutrientCreate, NutrientUpdate, Message


router = APIRouter(
    prefix="/nutrients",
    tags=["nutrients"]
)


@router.get("/", response_model=list[NutrientPublic])
def read_nutrients(
    nutrient_service: NutrientService = service_dep(NutrientService)
) -> list[NutrientPublic]:
    """
    Retreive nutrients.
    """
    return nutrient_service.repository.read()


@router.get("/{id}", response_model=NutrientPublic)
def read_nutrient(
    id: int,
    nutrient_service: NutrientService = service_dep(NutrientService),
) -> NutrientPublic:
    """
    Get nutrient by ID.
    """
    return nutrient_service.get(id)


@router.post("/", response_model=NutrientPublic)
def create_nutrient(
    nutrient_in: NutrientCreate,
    nutrient_service: NutrientService = service_dep(NutrientService),
) -> NutrientPublic:
    """
    Create new nutrient.
    """
    return nutrient_service.create(nutrient_in)


@router.put("/{id}", response_model=NutrientPublic)
def update_nutrient(
    id: int,
    nutrient_in: NutrientUpdate,
    nutrient_service: NutrientService = service_dep(NutrientService),
) -> NutrientPublic:
    """
    Update a nutrient.
    """
    return nutrient_service.update(id, nutrient_in)


@router.delete("/{id}")
def delete_nutrient(
    id: int,
    nutrient_service: NutrientService = service_dep(NutrientService),
) -> Message:
    """
    Delete a nutrient.
    """
    nutrient_service.delete(id)
    return Message(message="Nutrient deleted successfully")