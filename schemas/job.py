from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class JobCreate(BaseModel):
    title: str
    company: str
    location: str
    tech_stack: str
    description: Optional[str] = None

class JobResponse(BaseModel):
    id: int
    title: str
    company: str
    location: str
    tech_stack: str
    description: Optional[str]
    created_at: datetime

    class Config:
        from_attributes = True