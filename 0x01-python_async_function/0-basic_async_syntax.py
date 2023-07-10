#!/usr/bin/env python3
"""This module contains a coroutine"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """This function demonstrates an async operation"""
    time: float = random.uniform(0, max_delay)
    await asyncio.sleep(time)
    return time
