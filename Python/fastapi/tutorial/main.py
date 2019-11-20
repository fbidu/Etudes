from enum import Enum

from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

import uvicorn

app = FastAPI()


class Pokemon(str, Enum):
    PIKA = "pikachu"
    CHAR = "charmander"
    SQUI = "squirtle"


some_nice_people = [
    {"name": "Aline"},
    {"name": "Matheus"},
    {"name": "Melissa"},
    {"name": "Flávia"},
    {"name": "Ramalho"},
    {"name": "Fátima"},
    {"name": "Sandra"},
    {"name": "Osvaldo"},
    {"name": "まつもとゆきひろ"},
]


class ProgrammingLanguage(BaseModel):
    name: str
    description: str = None
    top_ten: bool
    year: int = None


@app.get("/")
async def root():
    return {"message": "First light!"}


@app.get("/typed/{item_id}")
async def typed(item_id: int):
    return {"id": item_id}


@app.get("/untyped/{item_id}")
async def untyped(item_id):
    return {"id": int(item_id)}


@app.get("/pokemon/{pokemon}")
async def poke(pokemon: Pokemon):
    result = {"pokemon": pokemon}
    if pokemon == Pokemon.PIKA:
        result["type"] = "electrical"

    if pokemon == Pokemon.CHAR:
        result["type"] = "fire"

    return result


@app.get("/amithere/{file_path:path}")
async def amithere(file_path):
    if file_path.startswith("/") or file_path.startswith(".."):
        raise HTTPException(403, {"message": "I see what you did there"})

    from pathlib import Path

    path = Path(file_path)

    return {"am_I_there": path.exists()}


@app.get("/nice_people")
async def nice_people(skip: int = 0, limit: int = 10):
    return some_nice_people[skip : skip + limit]


@app.post("/planguages/{item_id}")
async def create_language(item_id: int, item: ProgrammingLanguage, q: str = None):
    result = {"item_id": item_id, **item.dict()}
    if q:
        result.update({"q": q})

    return result


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port="8000")
