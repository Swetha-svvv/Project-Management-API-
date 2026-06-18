from pydantic import BaseModel, Field
from typing import Optional


class ProjectCreate(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)


class ProjectUpdate(BaseModel):
    name: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)


class ProjectResponse(BaseModel):
    id: int
    name: str
    description: Optional[str]

    class Config:
        from_attributes = True