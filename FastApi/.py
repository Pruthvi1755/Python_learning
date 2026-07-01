from fastapi import FastAPI
from pydantic import BaseModel

app=FastAPI()

class USER(BaseModel):
    name:str
    age:int
    password:int

class response(BaseModel):
    name:str
    age:int

@app.post("/user", response_model=response)
def user(user:USER):
    return {
        'name':"pruthvi",
        'age': 21,
        'password':12345678
    }