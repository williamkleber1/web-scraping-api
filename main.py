from typing import Union

from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/scrap/")
def search_client():
    return JSONResponse(content={"message": "Hello World"}, status_code=200)


