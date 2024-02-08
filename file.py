from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

class Database:
    elves = {}
    packages = {}

class Elf(BaseModel):
    name: str
    is_available: bool = True

class Package(BaseModel):
    content: str
    assigned_to: str = None

app = FastAPI()

@app.get("/elves/", response_model=List[Elf])
async def get_elves():
    return Database.elves.values()

@app.post("/elves/")
async def create_elf(elf: Elf):
    Database.elves[elf.name] = elf
    return elf

@app.put("/elves/{elf_name}")
async def update_elf(elf_name: str, elf: Elf):
    if elf_name not in Database.elves:
        raise HTTPException(status_code=404, detail="Elf not found")
    Database.elves[elf_name] = elf
    return elf

@app.delete("/elves/{elf_name}")
async def delete_elf(elf_name: str):
    if elf_name not in Database.elves:
        raise HTTPException(status_code=404, detail="Elf not found")
    del Database.elves[elf_name]
    return {"message": "Elf usunięty"}