# Write your corrected implementation for Task 3 here.
# Do not modify `task3.py`.
import math

def average_valid_measurements(values):
    if not values:
        return 0

    total = 0.0
    count = 0

    for v in values:
        if isinstance(v, (int, float)):
            if not math.isfinite(v):
                continue
            total += v
            count += 1

    return total / count if count else 0
