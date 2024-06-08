from typing import Union
from dotenv import dotenv_values
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from get_tools import get_tools
from pymongo import MongoClient
from routes import router as tool_router
from db import mongodb_client

app = FastAPI()

# Define our static folder, where will be our svelte build later
app.mount("/assets", StaticFiles(directory="public/assets"), name="static")

@app.on_event("shutdown")
def shutdown_db_client():
  mongodb_client.close()

app.include_router(tool_router, tags=["tools"], prefix="/api")

# Simply the root will return our Svelte build
@app.get("/", response_class=FileResponse)
async def main():
    return "public/index.html"
