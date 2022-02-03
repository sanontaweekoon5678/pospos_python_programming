from distutils.util import execute
from site import USER_SITE
from typing import Optional
from fastapi import FastAPI
from passlib.context import CryptContext

app = FastAPI()

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


users = {}


@app.get("/register")
def register(username: str, password: str):
    users[username] = get_password_hash(password)
    return users


@app.get("/login")
def login(username: str, password: str):
    try:
        hashed_password = users[username]
        if hashed_password and verify_password(password, hashed_password):
            return {"login": "ok"}
        else:
            return {"login": "invalid password"}
    except:
        return {"login": "invalid username"}
