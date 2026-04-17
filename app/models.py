from pydantic import BaseModel
from datetime import datetime

class Entry(BaseModel):
    username: str
    score: int
    timestamp: datetime