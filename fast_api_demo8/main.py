# from fastapi import FastAPI, Path

# app = FastAPI()


# @app.get("/items/{item_id}")
# async def read_items(
#     q: str, item_id: int = Path(..., title="The ID of the item to get")
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results


# app = FastAPI()


# @app.get("/items/{item_id}")
# async def read_items(
#     *, item_id: int = Path(..., title="The ID of the item to get"), q: str
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     return results

from fastapi import FastAPI, Path

app = FastAPI()


@app.get("/items/{item_id}")
async def read_items(
    *, item_id: int = Path(..., title="The ID of the item to get", gt=1, le=3), q: str
):
    results = {"item_id": item_id}
    if q:
        results.update({"q": q})
    return results
