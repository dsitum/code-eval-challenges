#!/usr/bin/env python3

import sys

def get_submission_score(score, memory_taken, time_taken, category):
    """
    @param score: the score which is received by test-cases
    @param memory_taken: memory taken by submission
    @param time_taken: time taken by submission
    @param category: Easy(1)/Moderate(2)/Hard(3)
    """

    total_max = {
        1: 35,  # max 35 points for Easy challenge
        2: 65,  # max 65 points for Moderate challenge
        3: 100  # max 100 points for Hard challenge
    }
    max_memory = 20 * 1024 * 1024  # 20 MB
    max_time = 10 * 1000  # 10 sec

    # if submission takes more than 10 seconds
    # or uses more than 20MB of memory
    # the score is 0
    if memory_taken > max_memory or time_taken > max_time:
        return 0

    max_total_score = total_max[category]

    memory_factor = 1 - memory_taken/max_memory
    time_factor = 1 - time_taken/max_time
    factor = (memory_factor + time_factor)/2

    return score * max_total_score * factor / 100


score = int(sys.argv[1])
time = int(sys.argv[2])
memory = int(sys.argv[3])
category = int(sys.argv[4])

print(get_submission_score(score, memory, time, category))