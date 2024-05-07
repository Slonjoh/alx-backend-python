#!/usr/bin/env python3
"""
Async Comprehensions
"""
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Asynchronous coroutine that collects 10 random float numbers
    using an asynchronous comprehension over async_generator.

    Returns:
    List[float]: A list containing 10 random float numbers.
    """
    # Asynchronous comprehension to collect 10 random numbers
    return [num async for num in async_generator()]
