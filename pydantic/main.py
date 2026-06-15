from fastapi import FastAPI
from fastapi import FastAPI
from pydantic import BaseModel

app= FastAPI()

# class User(BaseModel):
#     name: str
#     age: int
#     email: str

# @app.post("/create-user")
# def create_user(User: User):
#     return {"message": "User created successfully","data": User}

from pydantic import BaseModel


class Address(BaseModel):
    city: str
    pincode: str

class User(BaseModel):
    name: str
    age: int
    address: Address

@app.post("/create-user")
def create_user(user: User):
    return user