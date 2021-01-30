from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional


class Todo(BaseModel):
    Name: str
    Due_Date: str
    Description: str


app = FastAPI(title="Todo API")

store_todo = []


@app.get('/')  # Home
async def home():
    return {"Home": "Welcome Here!, 'Add a Todo on 127.0.0.1:8000/todo'"}


@app.put('/todo/')  # Create
async def create_todo(todo: Todo):
    store_todo.append(todo)
    return todo


@app.get('/todo/', response_model=List[Todo])  # Read
async def read_all_todo():
    return store_todo
