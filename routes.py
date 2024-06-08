from typing import List
from fastapi import APIRouter, Body, Request, Response, HTTPException, status
from fastapi.encoders import jsonable_encoder

from get_tools import get_tools
from models import ToolModel
from db import database
from pymongo import UpdateOne


router = APIRouter()

@router.get("/tools", response_description="List tools", response_model=List[ToolModel])
def list_tools(type: str | None = None, skip: int = 0, limit: int = -1):
  tools = list(database["tools"].find())
  if type:
    if type == "READ":
      return [tool for tool in tools if "READ" in tool["type"]][skip:skip + limit]
    elif type == "GITHUB REPO":
      return [tool for tool in tools if tool["type"] == "GITHUB REPO"][skip:skip + limit]
    elif type == "WEBSITE":
      return [tool for tool in tools if tool["type"] == "WEBSITE"][skip:skip + limit]
    elif type == "SPONSOR":
      return [tool for tool in tools if tool["type"] == "SPONSOR"][skip:skip + limit]

  return tools[skip:skip + limit]

@router.get("/update", response_description="Update tools list", response_model=List[str])
def update_tools():
  fetched_tools = get_tools()
  return insert_tools(fetched_tools)


def insert_tools(tools: List[ToolModel]):
    try:
        operations = [
            UpdateOne(
                {"url": item.url},  # filter by the unique field(s)
                {"$setOnInsert": item.dict()},  # only insert if the document does not exist
                upsert=True
            ) for item in tools
        ]

        if operations:
            result = database["tools"].bulk_write(operations)
            summary = [
                f"Inserted: {result.upserted_count} documents",
                f"Matched: {result.matched_count} documents",
                f"Modified: {result.modified_count} documents"
            ]
            return summary
        else:
            return ["No operations to perform"]
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
