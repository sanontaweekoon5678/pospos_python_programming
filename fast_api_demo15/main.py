from typing import Optional, List

from fastapi import FastAPI, Header
from fastapi.staticfiles import StaticFiles

app = FastAPI()


# @app.get("/items/")
# async def read_items(user_agent: Optional[str] = Header(None, convert_underscores=False)):
#     return {"User-Agent": user_agent}
#
# async def read_items(x_token: Optional[List[str]] = Header(None)):
#     return {"X-Token values": x_token}

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/items/")
async def read_items(Authorization: Optional[List[str]] = Header(None)):
    return {"Authorization": Authorization}
