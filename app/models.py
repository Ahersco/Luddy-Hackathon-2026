from pydantic import BaseModel
from datetime import datetime

class Entry(BaseModel):
    username: int
    score: str
    timestamp: datetime