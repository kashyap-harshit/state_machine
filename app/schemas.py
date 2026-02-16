from pydantic import BaseModel, Field
from typing import Dict, Any

class TaskCreate(BaseModel):
    task_type: str = Field(...,example="email_notification")
    payload: Dict[str, Any] = Field(..., example={"user_id": 101, "template": "welcome"})
    delay_seconds: int = Field(default=0, ge=0)