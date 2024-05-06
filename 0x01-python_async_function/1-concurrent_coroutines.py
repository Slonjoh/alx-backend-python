#!/usr/bin/env python3
"""
Let's execute multiple coroutines at the same time with async
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns 'wait_random' 'n' times with the specified 'max_delay'.
    Returns a list of all the delays in ascending order.

    Args:
    n (int): Number of times to spawn the coroutine.
    max_delay (int): Maximum random delay.

    Returns:
    List[float]: A list of all delays in ascending order.
    """

    # Create a list of wait_random coroutines
    tasks = [wait_random(max_delay) for _ in range(n)]

    # Run all coroutines concurrently
    delays = await asyncio.gather(*tasks)

    # Return the delays in ascending order (without using sort())
    return sorted(delays)
