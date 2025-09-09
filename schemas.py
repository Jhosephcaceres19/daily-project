from pydantic import BaseModel
from datetime import date, datetime
from typing import Optional

class UserCreate(BaseModel):
    name: str
    email: str
    role: str = "member"

class DailyCreate(BaseModel):
    date: date

class DailyResponseCreate(BaseModel):
    daily_id: int
    user_id: int
    did_today: str
    do_tomorrow: str
    blockers: Optional[str] = None
