# AI Agent Instructions for VibeCoding Course Project

## Project Overview
This is a FastAPI-based meal/recipe application that will allow users to discover random meals and recipes. The project is structured as a modern Python web application with an emphasis on clean architecture and user experience.

## Key Architecture Components
- **Framework**: FastAPI for building the REST API
- **Data Models**: Will use Pydantic V2 for data validation and serialization
- **External Integration**: Will integrate with an external meal/recipe API

## Project Structure
```
.
├── .github/          # GitHub related configurations
├── .llms/           # LLM-specific files (specs, plans)
│   └── specs/       # User story specifications
└── main.py         # FastAPI application entry point
```

## Development Workflows

### Setting Up Development Environment (with uv)
```bash
uv sync
source .venv/bin/activate

uv run uvicorn main:app --reload 
```

### Setting Up Development Environment (without uv)

```bash
# Install dependencies
pip install fastapi uvicorn

# Run the development server
uvicorn main:app --reload
```

### API Endpoints
- `GET /random-meal` - 


## Project-Specific Patterns

### Specs Implementation Pattern
1. Specifications are stored in `.llms/specs/` as Markdown files
2. Follow the pattern in `get_by_name_spec.md` for acceptance criteria

## Integration Points
- External meal/recipe API (to be integrated)
- FastAPI's automatic OpenAPI/Swagger documentation at `/docs`

## To Be Implemented
1. Database models and migrations
2. Error handling middleware
3. Authentication system


## Best Practices
- Use type hints consistently as shown in `main.py`
- Follow FastAPI's dependency injection pattern for upcoming features
- Document API endpoints using FastAPI's built-in docstring support