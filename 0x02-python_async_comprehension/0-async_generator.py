#!/usr/bin/env python3
"""
Async Generator
"""
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """
    Asynchronous coroutine that loops 10 times, waits 1 second,
    and then yields a random float number between 0 and 10.
    """
    for _ in range(10):
        # Asynchronous 1-second delay
        await asyncio.sleep(1)
        # Yield a random float between 0 and 10
        yield random.uniform(0, 10)
