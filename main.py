# Python imports
from typing import Optional
from enum import Enum

# Third party imports
from pydantic import BaseModel
from pydantic import Field

# FastAPI imports
from fastapi import FastAPI
from fastapi import Body, Query, Path

app = FastAPI()


# Pydantic models

class HairColor(Enum):
    black = "black"
    brown = "brown"
    blonde = "blonde"
    red = "red"
    white = "white"
    gray = "gray"
    other = "other"


class Person(BaseModel):
    first_name: str = Field(..., min_length=2, max_length=10)
    last_name: str = Field(..., min_length=2, max_length=10)
    age: int = Field(..., gt=0, lt=100)
    hair_color: Optional[HairColor] = Field(None)
    is_married: Optional[bool] = Field( None)

    class Config:
        schema_extra = {
            "example": {
                "first_name": "John",
                "last_name": "Doe",
                "age": 35,
                "hair_color": "brown",
                "is_married": True
            }
        }


@app.get("/")
def root():
    return {"message": "Hello World"}


# Request and response body
@app.post("/person/new")
def create_person(person: Person = Body(...)):
    return person


# validation query parameters

@app.get("/person/details")
def get_person_details(
    name: Optional[str] = Query(None, min_length=2, max_length=10),
    age: Optional[str] = Query(None),
):
    return {
        "name": name,
        "age": age
    }


# Validation path parameters
@app.get("/person/details/{person_id}")
def get_person_details(
    person_id: int = Path(..., gt=0),
    name: Optional[str] = Query(None, min_length=2, max_length=10),
):
    return {
        "person_id": person_id,
        "name": name
    }


# Validation body
@app.put("/person/{person_id}")
def update_person(
    person_id: int = Path(
        ...,
        gt=0,
        title="The ID of the person to get",
        description="Some long description",
    ),
    person: Person = Body(...)
):
    return person
