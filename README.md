# vibecoding-course

## Setup

### Using uv (recommended)
```bash
uv sync
```

### Using standard Python venv
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -e .


## Running the Project

### Using uv
```bash
uv run uvicorn main:app --reload
```

### Using standard Python
```bash
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`. Visit `http://localhost:8000/docs` for the interactive API documentation.
