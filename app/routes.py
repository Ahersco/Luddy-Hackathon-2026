from fastapi import APIRouter
from datetime import datetime
from app.models import Entry
from app.services import add_entry, get_top_10, leaderboard
from app.utils import compute_stats

router = APIRouter()

@router.post("/add")
def add(username: str, score: int):
    entry = Entry(username=username, score=score, timestamp=datetime.now())
    add_entry(entry)
    return {"message": "Added"}

@router.delete("/remove")
def remove(username: str):
    remove_entry(username)
    return {"message": "Removed"}

@router.get("/leaderboard")
def leaderboard_route():
    return get_top_10()

@router.get("/info")
def info():
    return compute_stats(leaderboard)