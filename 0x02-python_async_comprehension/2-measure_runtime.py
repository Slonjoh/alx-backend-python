#!/usr/bin/env python3
"""
Run time for four parallel comprehensions
"""
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Measures the total runtime to run 'async_comprehension'
    four times in parallel.

    Returns:
    float: Total runtime in seconds.
    """
    # Record the start time
    start = time.perf_counter()

    # Run 'async_comprehension' four times concurrently
    await asyncio.gather(
        async_comprehension(),  # First instance
        async_comprehension(),  # Second instance
        async_comprehension(),  # Third instance
        async_comprehension()   # Fourth instance
    )

    # Record the end time
    end = time.perf_counter()

    # Calculate the total elapsed time
    return end - start  # Return the total runtime
