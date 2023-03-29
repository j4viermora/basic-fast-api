# Python imports
from typing import Optional

# Third party imports
from pydantic import BaseModel

# FastAPI imports
from fastapi import FastAPI
from fastapi import Body
from fastapi import Query
from fastapi import Path

app = FastAPI()


# Pydantic model
class Person(BaseModel):
    first_name: str
    last_name: str
    age: int
    hair_color: Optional[str] = None
    is_married: Optional[bool] = None


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
