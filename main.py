from typing import Union
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from usercase.scrap_page import *

app = FastAPI()
scraper = JobScraper()


@app.get("/scrap/")
def search_client():
    scraper.execute()
    return JSONResponse(content={"message": "Hello World"}, status_code=200)


