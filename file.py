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

#======================================PACZKI===================================

@app.get("/packages/", response_model=List[Package])
async def get_packages():
    return Database.packages.values()

@app.post("/packages/")
async def create_package(package: Package):
    Database.packages[len(Database.packages) + 1] = package
    return package

@app.put("/packages/{package_id}")
async def update_package(package_id: int, package: Package):
    if package_id not in Database.packages:
        raise HTTPException(status_code=404, detail="Package not found")
    Database.packages[package_id] = package
    return package

@app.delete("/packages/{package_id}")
async def delete_package(package_id: int):
    if package_id not in Database.packages:
        raise HTTPException(status_code=404, detail="Package not found")
    del Database.packages[package_id]
    return {"message": "Paczka usunięta"}