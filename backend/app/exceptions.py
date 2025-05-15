from abc import ABC

from fastapi import HTTPException, status


class NotFoundException(HTTPException, ABC):
    """
        Base exception class for all "Not found" 
    """
    def __init__(self, resource_name: str) -> None:
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{resource_name} not found"
        )


class NutrientNotFound(NotFoundException):
    def __init__(self) -> None:
        super().__init__(resource_name='Nutrient')


class RecipeNotFound(NotFoundException):
    def __init__(self) -> None:
        super().__init__(resource_name='Recipe')