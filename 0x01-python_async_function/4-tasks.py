#!/usr/bin/env python3
"""
Contains a method that spawns Tasks n times with a
specified delay between each call
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns 'task_wait_random' 'n' times with the specified 'max_delay'.
    Returns a list of all the delays in ascending order.

    Args:
    n (int): Number of times to spawn the coroutine.
    max_delay (int): Maximum random delay.

    Returns:
    List[float]: A list of all delays in ascending order.
    """
    # Create a list of asyncio tasks
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # Run all tasks concurrently and await their results
    results = await asyncio.gather(*tasks)

    # Return the results in ascending order
    return sorted(results)
