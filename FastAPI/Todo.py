from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List


class Todo(BaseModel):
    Name: str
    Due_Date: str
    Description: str


app = FastAPI(title="Todo API")

store_todo = []


@ app.get('/')  # Home
async def home():
    return {"Home": "Welcome Here!, 'Add a Todo on 127.0.0.1:8000/todo'"}


@ app.post('/todo/')  # Create
async def create_todo(todo: Todo):
    store_todo.append(todo)
    return todo


@ app.get('/todo/', response_model=List[Todo])  # Read
async def read_all_todo():
    return store_todo


@app.get('/todo/{id}')
async def get_todo(id: int):
    try:
        return store_todo[id-1]
    except:
        raise HTTPException(status_code=404, details="Todo Not Found")


@app.put('/todo/{id}')
async def update_todo(id: int, todo: Todo):
    try:
        store_todo[id] = todo
        return store_todo[id]
    except:
        raise HTTPException(status_code=404, details="Todo Not Found")


@app.delete('/todo/{id}')
async def delete_todo(id: int):
    try:
        obj = store_todo[id]
        store_todo.pop(id)
        return obj
    except:
        raise HTTPException(status_code=404, details="Todo Not Found")
