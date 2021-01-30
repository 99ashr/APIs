from pydantic import BaseModel
from typing import Optional
from fastapi import FastAPI

app = FastAPI()


class Package(BaseModel):
    name: str
    number: int
    Description: Optional[str] = None


@app.get('/')
async def hello():
    return {'Hello': 'World'}


@app.post('/package/{priority}')
async def make_package(priority: int, package: Package, value: bool):
    return {'priority': priority, **package.dict(), 'value': value}

# -------------------------- Try it out(additional) -------------------------- #


@app.get("/ component/{para}")  # @path parameter
async def component(component_id: int):
    return {"ID": component_id}


@app.get("/component/")  # @query parameter
async def read_component(number: int, text: Optional[str]):
    return{"number": number, "text": text}
# ---------------------------------------------------------------------------- #
