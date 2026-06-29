from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    id: int
    title: str
    description: str

@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return {"message": "Todo created successfully"}

@app.get("/todos")
def get_todos():
    return todos

@app.get("/todos/{id}")
def get_info(id: int):
    for todo in todos:
        if todo.id == id:
            return todo

    return {"message": "Todo not found"}

