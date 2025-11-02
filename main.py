from fastapi import FastAPI
import httpx

app = FastAPI()


@app.get("/random-meal")
async def get_random_meal():
    async with httpx.AsyncClient() as client:
        response = await client.get(
            "https://www.themealdb.com/api/json/v1/1/random.php"
        )

    if response.status_code != 200:
        return {"error": "Falha ao carregar refeição aleatória"}

    data = response.json()
    meal = data["meals"][0]

    return {
        "nome": meal["strMeal"],
        "ingredientes": [
            ingrediente
            for ingrediente in (
                meal["strIngredient1"],
                meal["strIngredient2"],
                meal["strIngredient3"],
            )
            if ingrediente
        ],
        "instruções": [
            instrução
            for instrução in (meal["strInstructions"].splitlines()[:5])
            if instrução
        ],
    }
