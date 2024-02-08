from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

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