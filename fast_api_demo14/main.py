from distutils.util import execute
from typing import Optional

from fastapi import FastAPI
from pydantic import BaseModel, EmailStr

app = FastAPI()


class UserIn(BaseModel):
    username: str
    password: str
    email: EmailStr
    full_name: Optional[str] = None


# class UserOut(BaseModel):
#     username: str
#     email: EmailStr
#     full_name: Optional[str] = None


@app.post("/user/", response_model=UserIn, response_model_exclude={"password"})
async def create_user(user: UserIn):
    return user
