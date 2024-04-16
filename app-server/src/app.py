from fastapi import FastAPI
from fastapi.responses import HTMLResponse

import pathlib

app = FastAPI(title="NGINX Test")

local = pathlib.Path(__file__).parent / "web"

def get_page() -> str:
    with open(local / "index.html", "r") as file:
        return file.read() 

@app.get("/", response_class=HTMLResponse)
async def root():
    page = get_page()
    return HTMLResponse(page)
