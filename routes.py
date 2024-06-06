from typing import List
from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder

from get_tools import get_tools
from models import ToolModel
from db import database

router = APIRouter()

@router.get("/", response_description="List all tools", response_model=List[ToolModel])
def list_tools():
  tools = list(database["tools"].find())
  return tools

@router.get("/update", response_description="Update tools list", response_model=List[ToolModel])
def update_tools():
  fetched_tools = get_tools()
  tools = database["tools"].insert_many(fetched_tools)
  return list(fetched_tools)
