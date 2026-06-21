# Todo App API

A simple REST API for managing todos, built with FastAPI and SQLite.

## Tech Stack

- **Python** — Programming language
- **FastAPI** — Web framework
- **SQLAlchemy** — ORM
- **SQLite** — Database
- **Pydantic** — Data validation

## Features

- Create, read, update, and delete todos
- Partial updates (update only the fields you send)
- Mark todos as complete/incomplete via update endpoint

## Installation

**1. Clone the repository**
```bash
git clone https://github.com/developerhinakhan/todo-app-crud.git
cd todo-app-crud
```

**2. Create virtual environment**
```bash
python -m venv myenv
source myenv/Scripts/activate
```

**3. Install dependencies**
```bash
pip install fastapi uvicorn sqlalchemy pydantic
```

**4. Run the server**
```bash
uvicorn main:app --reload
```

**5. Open Swagger UI**
```
http://127.0.0.1:8000/docs
```

## API Endpoints

### Todos
- `POST /todos` — Create a new todo
- `GET /todos` — List all todos
- `GET /todos/{id}` — Get a single todo
- `PUT /todos/{id}` — Update a todo (partial updates supported)
- `DELETE /todos/{id}` — Delete a todo

## Developer

**Hina Noor**
Python Backend Developer
GitHub: [developerhinakhan](https://github.com/developerhinakhan)
