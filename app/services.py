from datetime import datetime
from typing import List
from models import Entry

leaderboard: List[Entry] = []
performance_log = {}

entry_given = False

def add_entry(entry: Entry):
    leaderboard.append(entry)
    performance_log[entry.username] = entry.score

def remove_entry(username: str):
    global leaderboard
    leaderboard = [entry for entry in leaderboard if entry.username != username]
    if username in perfromance_log:
        del perfromance_log[username]

def get_top_10():
    sorted_leaderboard = sorted(leaderbooard, key=lambda x: x.score, reverse=True)
    return sorted_leaderboard[:10]

name = input("Enter username: ")
score = input("Enter score: ")
date = datetime.now()
entry = Entry(username=name, score=int(score), timestamp=date)
add_entry(entry)

def filter_by_user(username: str):
    return [entry for entry in leaderboard if entry.username == username]

def filter_by_time(start_time: datetime, end_time: datetime):
    return [
        entry for entry in leaderboard
        if start_time <= entry.timestamp <= end_time
    ]

def filte_by_score(min_score: int, max_score: int):
    return [
        entry for entry in leaderboard
        if min_score <= entry.score <= max_score
    ]