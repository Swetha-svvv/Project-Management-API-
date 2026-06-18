from typing import Optional

from pydantic import BaseModel, Field

from src.database.models import TaskStatus


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)
    status: TaskStatus = TaskStatus.TODO


class TaskUpdate(BaseModel):
    title: str = Field(..., min_length=3, max_length=100)
    description: Optional[str] = Field(default=None, max_length=500)
    status: TaskStatus


class TaskResponse(BaseModel):
    id: int
    title: str
    description: Optional[str]
    status: TaskStatus

    class Config:
        from_attributes = True