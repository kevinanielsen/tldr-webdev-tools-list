from typing import Union
from dotenv import dotenv_values
from fastapi import FastAPI
from get_tools import get_tools
from pymongo import MongoClient
from routes import router as tool_router
from db import mongodb_client


app = FastAPI()

@app.on_event("shutdown")
def shutdown_db_client():
  mongodb_client.close()

app.include_router(tool_router, tags=["tools"], prefix="/tools")
