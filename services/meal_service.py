"""Service module that encapsulates the external API call and JSON parsing
for fetching a random meal.

This keeps the endpoint handler small and makes the logic testable.
Now uses Pydantic V2 schemas for type safety and validation.
"""

import httpx
from pydantic import ValidationError

from schemas.meal import (
    ErrorResponse,
    RandomMealResponse,
    TheMealDBResponse,
)


class ExternalAPIError(Exception):
    """Custom exception for external API failures."""

    pass


def fetch_random_meal_from_api() -> RandomMealResponse | ErrorResponse:
    """Fetch a random meal from TheMealDB and return a validated response.

    Returns:
        RandomMealResponse: Validated meal data with all ingredients
        ErrorResponse: Error information if the request fails

    Raises:
        ExternalAPIError: When the external API request fails
        ValidationError: When the API response doesn't match expected schema
    """
    try:
        with httpx.Client() as client:
            response = client.get(
                "https://www.themealdb.com/api/json/v1/1/random.php",
                timeout=10.0,
            )

        if response.status_code != 200:
            return ErrorResponse(
                error="Falha ao carregar refeição aleatória",
                detail=(
                    f"HTTP {response.status_code}: {response.reason_phrase}"
                ),
            )

        # Parse and validate the external API response
        try:
            data = response.json()
            themealdb_response = TheMealDBResponse.model_validate(data)
        except ValidationError as e:
            return ErrorResponse(
                error="Resposta inválida da API externa",
                detail=f"Validation error: {str(e)}",
            )
        except Exception as e:
            return ErrorResponse(
                error="Erro ao processar resposta da API",
                detail=str(e),
            )

        # Check if meals list exists and has at least one meal
        if not themealdb_response.meals or len(themealdb_response.meals) == 0:
            return ErrorResponse(
                error="Resposta inválida da API externa",
                detail="No meals returned from API",
            )

        # Get the first meal and transform to internal response format
        meal = themealdb_response.meals[0]
        return RandomMealResponse.from_themealdb_meal(meal)

    except httpx.RequestError as e:
        return ErrorResponse(
            error="Falha ao conectar com a API externa",
            detail=f"Request error: {str(e)}",
        )
    except Exception as e:
        return ErrorResponse(
            error="Erro inesperado ao buscar refeição",
            detail=str(e),
        )
