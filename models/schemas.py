from pydantic import BaseModel
from typing import Optional
from datetime import datetime

# Request schema for creating an interview session
class InterviewSessionCreate(BaseModel):
    user_id: int
    job_role: str
    experience_level: str
    company: Optional[str] = None

# Response schema for returning interview session details
class InterviewSessionResponse(InterviewSessionCreate):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True  # Ensures compatibility with ORM models
