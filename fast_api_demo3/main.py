from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel


class User(BaseModel):
    username: str
    password: str


app = FastAPI()


@app.post("/login")
def post_login():
    return {"login": "yes"}


@app.post("/register")
def post_register(user):
    return {"register": user}
