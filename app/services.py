from typing import List
from .models import Entry

leaderbooard: List[Entry] = []
perfromance_log = {}

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