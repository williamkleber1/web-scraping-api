from typing import Union
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
import asyncio



from usercase.scrap_page import *

app = FastAPI()
scraper = JobScraper()

app.mount("/static", StaticFiles(directory="output"), name="static")

@app.get("/scrap/")
def search_client():
    scraper.execute()
    return JSONResponse(content={"message": "Hello World"}, status_code=200)

@app.get("/", response_class=HTMLResponse)
async def read_report():
    loop = asyncio.get_event_loop()
    await loop.run_in_executor(None, scraper.execute)
    
    with open("output/index.html", "r") as file:
        html_content = file.read()
    
    # Inserindo a tabela HTML
    with open("output/tabela_vagas.html", "r") as tabela_file:
        tabela_html = tabela_file.read()
    html_content = html_content.replace("<!--TABELA-->", tabela_html)
    
    return HTMLResponse(content=html_content)


