from typing import Optional
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def hello():
    return {'Hello': 'World'}


@app.get("/ component/{para}")
async def component(component_id):
    return {"ID": "component_id"}
