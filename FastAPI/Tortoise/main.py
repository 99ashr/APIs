from fastapi import FastAPI, HTTPException
from typing import List
from model import Todo_Pydantic, TodoIn_Pydantic, Todo
from tortoise.contrib.fastapi import HTTPNotFoundError, register_tortoise


app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/todo/", response_model=Todo_Pydantic)
async def create(todo: TodoIn_Pydantic):
    obj = await Todo.create(**todo.dict(exclude_unset=True))
    return await Todo_Pydantic.from_tortoise_orm(obj)

register_tortoise(
    app,
    db_url="sqlite://store.db",
    modules={'model': ['model']},
    generate_schemas=True,
    add_exception_handlers=True,
)
