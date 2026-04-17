import statistics
import time

def calc_stats(entries):
    scores = [entry.score for entry in entries]
    mean_score = statistics.mean(scores)
    median_score = statistics.median(scores)
    stdev_score = statistics.stdev(scores) if len(scores) > 1 else 0
    return mean_score, median_score, stdev_score

def track_performance(username, score):
    start_time = time.time()
    # Simulate some processing
    time.sleep(0.1)
    end_time = time.time()
    duration = end_time - start_time
    print(f"Performance for {username}: Score={score}, Time={duration:.2f} seconds")