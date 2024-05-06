#!/usr/bin/env python3
"""
Tasks
"""
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates an asyncio task to wait for a random delay.

    Args:
    max_delay (int): Maximum delay in seconds.

    Returns:
    asyncio.Task: A task that can be awaited to complete the
    wait_random coroutine.
    """
    # Create and return an asyncio task
    return asyncio.create_task(wait_random(max_delay))
