from pydantic import BaseModel
from typing import Optional

class TaskRequest(BaseModel):
    prompt: str

class TaskResponse(BaseModel):
    assigned_agent: str
    result: str
    status: str = "success"
