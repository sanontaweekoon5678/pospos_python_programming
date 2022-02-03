from fastapi import FastAPI
from fastapi.responses import FileResponse

some_file_path = "readme.txt"
app = FastAPI()


@app.get("/")
def main():
    return FileResponse(some_file_path)


@app.get("/download")
def download():
    return FileResponse(path="./readme.txt", media_type='text/plain', filename=some_file_path)
