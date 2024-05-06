#!/usr/bin/env python3
"""
Measure the runtime
"""
import time
import asyncio
from typing import Tuple

# Importing wait_n from previous file
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
    Measures the average execution time for 'wait_n(n, max_delay)'.

    Args:
    n (int): Number of times to spawn the coroutine.
    max_delay (int): Maximum random delay.

    Returns:
    float: The average time it takes for each coroutine to complete.
    """

    # Record the start time
    start = time.perf_counter()

    # Run the wait_n coroutine
    asyncio.run(wait_n(n, max_delay))

    # Record the end time
    end = time.perf_counter()

    # Calculate the total elapsed time
    total_time = end - start

    # Return the average time per coroutine
    return total_time / n
