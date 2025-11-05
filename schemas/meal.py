"""Pydantic V2 schemas for meal-related data structures.

This module defines schemas for:
- External API responses from TheMealDB
- Internal API responses for the application
- Error responses
"""

from typing import Self

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    field_validator,
    model_validator,
)


class Ingredient(BaseModel):
    """Represents a single ingredient with its measurement."""

    nome: str = Field(..., description="Nome do ingrediente")
    medida: str = Field(..., description="Medida/quantidade do ingrediente")

    model_config = ConfigDict(
        str_strip_whitespace=True,
        json_schema_extra={
            "example": {"nome": "Chicken", "medida": "500g"}
        },
    )


class TheMealDBMeal(BaseModel):
    """Schema for a single meal from TheMealDB API.

    Maps all 20 ingredient and measure fields from the external API.
    """

    id_meal: str = Field(alias="idMeal")
    str_meal: str = Field(alias="strMeal")
    str_instructions: str = Field(alias="strInstructions")
    str_meal_thumb: str | None = Field(default=None, alias="strMealThumb")

    # All 20 ingredient fields
    str_ingredient1: str | None = Field(default=None, alias="strIngredient1")
    str_ingredient2: str | None = Field(default=None, alias="strIngredient2")
    str_ingredient3: str | None = Field(default=None, alias="strIngredient3")
    str_ingredient4: str | None = Field(default=None, alias="strIngredient4")
    str_ingredient5: str | None = Field(default=None, alias="strIngredient5")
    str_ingredient6: str | None = Field(default=None, alias="strIngredient6")
    str_ingredient7: str | None = Field(default=None, alias="strIngredient7")
    str_ingredient8: str | None = Field(default=None, alias="strIngredient8")
    str_ingredient9: str | None = Field(default=None, alias="strIngredient9")
    str_ingredient10: str | None = Field(default=None, alias="strIngredient10")
    str_ingredient11: str | None = Field(default=None, alias="strIngredient11")
    str_ingredient12: str | None = Field(default=None, alias="strIngredient12")
    str_ingredient13: str | None = Field(default=None, alias="strIngredient13")
    str_ingredient14: str | None = Field(default=None, alias="strIngredient14")
    str_ingredient15: str | None = Field(default=None, alias="strIngredient15")
    str_ingredient16: str | None = Field(default=None, alias="strIngredient16")
    str_ingredient17: str | None = Field(default=None, alias="strIngredient17")
    str_ingredient18: str | None = Field(default=None, alias="strIngredient18")
    str_ingredient19: str | None = Field(default=None, alias="strIngredient19")
    str_ingredient20: str | None = Field(default=None, alias="strIngredient20")

    # All 20 measure fields
    str_measure1: str | None = Field(default=None, alias="strMeasure1")
    str_measure2: str | None = Field(default=None, alias="strMeasure2")
    str_measure3: str | None = Field(default=None, alias="strMeasure3")
    str_measure4: str | None = Field(default=None, alias="strMeasure4")
    str_measure5: str | None = Field(default=None, alias="strMeasure5")
    str_measure6: str | None = Field(default=None, alias="strMeasure6")
    str_measure7: str | None = Field(default=None, alias="strMeasure7")
    str_measure8: str | None = Field(default=None, alias="strMeasure8")
    str_measure9: str | None = Field(default=None, alias="strMeasure9")
    str_measure10: str | None = Field(default=None, alias="strMeasure10")
    str_measure11: str | None = Field(default=None, alias="strMeasure11")
    str_measure12: str | None = Field(default=None, alias="strMeasure12")
    str_measure13: str | None = Field(default=None, alias="strMeasure13")
    str_measure14: str | None = Field(default=None, alias="strMeasure14")
    str_measure15: str | None = Field(default=None, alias="strMeasure15")
    str_measure16: str | None = Field(default=None, alias="strMeasure16")
    str_measure17: str | None = Field(default=None, alias="strMeasure17")
    str_measure18: str | None = Field(default=None, alias="strMeasure18")
    str_measure19: str | None = Field(default=None, alias="strMeasure19")
    str_measure20: str | None = Field(default=None, alias="strMeasure20")

    model_config = ConfigDict(
        populate_by_name=True,
        str_strip_whitespace=True,
        extra="ignore",  # Ignore unknown fields from API
    )

    @field_validator(
        "str_ingredient1",
        "str_ingredient2",
        "str_ingredient3",
        "str_ingredient4",
        "str_ingredient5",
        "str_ingredient6",
        "str_ingredient7",
        "str_ingredient8",
        "str_ingredient9",
        "str_ingredient10",
        "str_ingredient11",
        "str_ingredient12",
        "str_ingredient13",
        "str_ingredient14",
        "str_ingredient15",
        "str_ingredient16",
        "str_ingredient17",
        "str_ingredient18",
        "str_ingredient19",
        "str_ingredient20",
        "str_measure1",
        "str_measure2",
        "str_measure3",
        "str_measure4",
        "str_measure5",
        "str_measure6",
        "str_measure7",
        "str_measure8",
        "str_measure9",
        "str_measure10",
        "str_measure11",
        "str_measure12",
        "str_measure13",
        "str_measure14",
        "str_measure15",
        "str_measure16",
        "str_measure17",
        "str_measure18",
        "str_measure19",
        "str_measure20",
        mode="before",
    )
    @classmethod
    def clean_empty_strings(cls, v: str | None) -> str | None:
        """Convert empty or whitespace-only strings to None."""
        if v is None:
            return None
        stripped = v.strip()
        return stripped if stripped else None

    def get_ingredients(self) -> list[Ingredient]:
        """Extract all non-empty ingredients with their measures.

        Returns:
            List of Ingredient objects with nome and medida fields.
        """
        ingredients = []
        for i in range(1, 21):
            ingredient_name = getattr(self, f"str_ingredient{i}")
            measure = getattr(self, f"str_measure{i}")

            if ingredient_name:
                ingredients.append(
                    Ingredient(
                        nome=ingredient_name,
                        medida=measure if measure else "",
                    )
                )

        return ingredients


class TheMealDBResponse(BaseModel):
    """Schema for the top-level response from TheMealDB API."""

    meals: list[TheMealDBMeal] | None = None

    model_config = ConfigDict(
        extra="ignore",
    )

    @model_validator(mode="after")
    def validate_meals(self) -> Self:
        """Ensure meals list is not empty if present."""
        if self.meals is not None and len(self.meals) == 0:
            raise ValueError("meals list cannot be empty")
        return self


class RandomMealResponse(BaseModel):
    """Internal API response schema for a random meal.

    Uses Portuguese field names for consistency with the application.
    """

    nome: str = Field(..., description="Nome da refeição")
    ingredientes: list[Ingredient] = Field(
        ..., description="Lista de ingredientes com medidas"
    )
    instrucoes: list[str] = Field(
        ..., description="Instruções de preparo (linhas não vazias)"
    )
    imagem: str | None = Field(
        default=None, description="URL da imagem da refeição"
    )
    id: str = Field(..., description="ID da refeição")

    model_config = ConfigDict(
        str_strip_whitespace=True,
        json_schema_extra={
            "example": {
                "nome": "Chicken Curry",
                "ingredientes": [
                    {"nome": "Chicken", "medida": "500g"},
                    {"nome": "Curry Powder", "medida": "2 tbsp"},
                ],
                "instrucoes": [
                    "Heat oil in a pan",
                    "Add chicken and cook until brown",
                ],
                "imagem": (
                    "https://www.themealdb.com/images/media/meals/1234.jpg"
                ),
                "id": "52772",
            }
        },
    )

    @classmethod
    def from_themealdb_meal(cls, meal: TheMealDBMeal) -> "RandomMealResponse":
        """Create a RandomMealResponse from a TheMealDBMeal.

        Args:
            meal: The external API meal object

        Returns:
            RandomMealResponse with transformed data
        """
        # Extract all non-empty ingredients
        ingredientes = meal.get_ingredients()

        # Split instructions by lines and filter empty ones
        instrucoes = [
            line.strip()
            for line in meal.str_instructions.splitlines()
            if line.strip()
        ]

        return cls(
            nome=meal.str_meal,
            ingredientes=ingredientes,
            instrucoes=instrucoes,
            imagem=meal.str_meal_thumb,
            id=meal.id_meal,
        )


class ErrorResponse(BaseModel):
    """Standardized error response schema."""

    error: str = Field(..., description="Mensagem de erro")
    detail: str | None = Field(
        default=None, description="Detalhes adicionais do erro"
    )

    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "error": "Falha ao carregar refeição aleatória",
                "detail": "HTTP 500: Internal Server Error",
            }
        }
    )