from pydantic import BaseModel, Field
from datetime import datetime

class TaskInput(BaseModel):
    title: str
    description: str

class Task(TaskInput):
    category: str | None = None
    summary: str | None = None
    created_at: datetime