# User Story - Filtrar por Ingrediente Principal

## 🔍 US-004: Filtrar Refeições por Ingrediente Principal

**Como** usuário  
**Eu quero** filtrar refeições por um ingrediente principal específico  
**Para que** eu possa encontrar receitas que usem ingredientes que tenho disponíveis em casa

### Critérios de Aceite:

#### Técnico (FastAPI + Pydantic v2):
- [ ] Criar endpoint GET `/meals/filter` com query parameter `ingredient`
- [ ] Validar o parâmetro `ingredient` usando Pydantic (não vazio, tipo string)
- [ ] Criar modelo Pydantic `FilteredMealResponse` com campos: `idMeal`, `strMeal`, `strMealThumb`
- [ ] Criar modelo `FilteredMealsListResponse` contendo lista de meals
- [ ] Implementar tratamento de erro se a API externa retornar 400/500
- [ ] Adicionar timeout de 10s na requisição à API externa
- [ ] Documentação automática do endpoint deve estar disponível no Swagger (`/docs`)

#### Validações:
- [ ] Ingredient deve ter no mínimo 2 caracteres
- [ ] Caracteres especiais devem ser tratados corretamente (URL encoding)
- [ ] Response da API externa deve ser validado pelo modelo Pydantic

#### Performance:
- [ ] Implementar cache básico para ingredientes buscados recentemente (opcional)
- [ ] A busca deve retornar em menos de 3 segundos em condições normais

---

### 📝 Exemplo de Implementação (Referência):

```python
# models.py
from pydantic import BaseModel, Field

class FilteredMeal(BaseModel):
    id_meal: str = Field(alias="idMeal")
    name: str = Field(alias="strMeal")
    thumbnail: str = Field(alias="strMealThumb")

class FilteredMealsResponse(BaseModel):
    meals: list[FilteredMeal] | None

# endpoint.py
@router.get("/meals/filter", response_model=FilteredMealsResponse)
async def filter_meals_by_ingredient(
    ingredient: str = Query(..., min_length=2)
):
    # Implementation here
    pass
```

---

### 🎯 Definition of Done:
- Código revisado e aprovado
- Documentação da API atualizada
- Testado manualmente com diferentes ingredientes
- Deploy em ambiente de staging realizado