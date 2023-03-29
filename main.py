# Python imports
from typing import Optional

# Third party imports
from pydantic import BaseModel

# FastAPI imports
from fastapi import FastAPI
from fastapi import Body

app = FastAPI()



# Pydantic model
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/person/new")
async def create_person(person: Person = Body(...)):
    return person