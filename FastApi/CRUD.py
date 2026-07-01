from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    id: int
    title: str
    description: str

# create--
@app.post("/todos")
def create_todo(todo: Todo):
    todos.append(todo)
    return {"message": "Todo created successfully"}

# Read all--
@app.get("/todos")
def get_todos():
    return todos

# Read one--
@app.get("/todos/{id}")
def get_info(id: int):
    for todo in todos:
        if todo.id == id:
            return todo
    return {"message": "Todo not found"}

# Update--
@app.put("/todos/{id}")
def update(id:int, update:Todo):
    for i,todo in enumerate(todos):
        if todo.id == todo.id:
            todos[i] = update
            return{
                'id updated'
            }
        
# Delete--
@app.delete('/todos/{id}')
def delete(id:int):
    for i, todo in enumerate(todos):
        if todo.id == id:
            todos.pop(i)
            return {"deleted"}

