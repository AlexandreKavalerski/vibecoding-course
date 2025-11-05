from fastapi import FastAPI

from schemas.meal import ErrorResponse, RandomMealResponse
from services.meal_service import fetch_random_meal_from_api

app = FastAPI()


@app.get(
    "/random-meal",
    response_model=RandomMealResponse | ErrorResponse,
    responses={
        200: {
            "description": "Random meal successfully retrieved",
            "model": RandomMealResponse,
        },
        500: {
            "description": "Error retrieving meal from external API",
            "model": ErrorResponse,
        },
    },
)
def get_random_meal() -> RandomMealResponse | ErrorResponse:
    """Endpoint that returns a random meal using the service layer.

    Returns:
        RandomMealResponse: A random meal with all ingredients and instructions
        ErrorResponse: Error information if the request fails
    """
    return fetch_random_meal_from_api()
