from pydantic import BaseModel, ConfigDict, Field

class ToolModel(BaseModel):
  """
  Container for a single tool record.
  """

  title: str = Field(...)
  url: str = Field(...)
  type: str = Field(...)
  description: str = Field(...)
  class Config:
    allow_population_by_field_name = True
    schema_extra = {
        "example": {
          "title": "HTMX",
          "url": "https://htmx.org/",
          "description": "HTMX is a library for building interactive web applications using HTML, CSS, and JavaScript.",
          "type": "GITHUB REPO",
        }
    }
