from typing import List
from app.models import Entry
from datetime import datetime

leaderboard: List[Entry] = []
performance_log = {}

entry_given = False

def add_entry(entry: Entry):
    leaderboard.append(entry)
    performance_log[entry.username] = entry.score

def remove_entry(username: str):
    global leaderboard
    leaderboard = [entry for entry in leaderboard if entry.username != username]
    if username in performance_log:
        del performance_log[username]

def get_top_10():
    sorted_leaderboard = sorted(leaderboard, key=lambda x: x.score, reverse=True)
    return sorted_leaderboard[:10]

name = input("Enter username: ")
score = input("Enter score: ")
entry = Entry(username=name, score=int(score), timestamp=datetime.now())
add_entry(entry)
