from fastapi import APIRouter
from datetime import datetime
from app.models import Entry
from app.services import add_entry, get_top_10, leaderboard
from app.utils import compute_stats
from typing import Optional

router = APIRouter()

@router.post("/add")
def add(username: str, score: int):
    entry = Entry(username=username, score=score, timestamp=datetime.now())
    add_entry(entry)
    leaderboard.append(entry)
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

@router.get("/performance")
def performance():
    return {"performance": performance_log}

@router.get("/sort1")
def sort_by_score():
    sorted_leaderboard = sorted(leaderboard, key=lambda x: x.score, reverse=True)
    return sorted_leaderboard

@router.get("/sort2")
def sort_by_time():
    sorted_leaderboard = sorted(leaderboard, key=lambda x: x.timestamp, reverse=True)
    return sorted_leaderboard

@router.get("/sort3")
def sort_by_username():
    sorted_leaderboard = sorted(leaderboard, key=lambda x: x.username)
    return sorted_leaderboard

@router.get("/history")
def history(
    username: Optional[str] = None,
    start_time: Optional[str] = None,
    end_time: Optional[str] = None
):
    results = leaderboard

    # Filter by username
    if username:
        results = [e for e in results if e["username"] == username]

    # Filter by start time
    if start_time:
        start = datetime.fromisoformat(start_time)
        results = [
            e for e in results
            if datetime.fromisoformat(e["timestamp"]) >= start
        ]

    # Filter by end time
    if end_time:
        end = datetime.fromisoformat(end_time)
        results = [
            e for e in results
            if datetime.fromisoformat(e["timestamp"]) <= end
        ]

    return results