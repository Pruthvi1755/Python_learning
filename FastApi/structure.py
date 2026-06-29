from fastapi import FastAPI
from pydantic import BaseModel
app = FastAPI()

# @app.get("/")
# def home():
#     return {"message": "Welcome to the FastAPI application!"}

# class Address(BaseModel):
#     pin: int
#     city: str
#     region: str

# class User(BaseModel):
#     name: str
#     age: int
#     address: Address

# @app.post("/user")
# def create_user(user:User):
#     return user