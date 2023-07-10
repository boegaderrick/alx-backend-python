#!/usr/bin/env python3
"""This module contains an asyncronous function"""
from asyncio import gather
from typing import Callable, List

task_wait_random: Callable = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
        This function calls `asyncio.gather` with a tuple containing the return
        of multiple calls to the imported `task_wait_random` function as the
        parameter. The return of `asyncio.gather()` is awaited before it gets
        sorted then returned to the caller.
    """
    ret: List[float]

    ret = await gather(*(task_wait_random(max_delay) for _ in range(n)))

    return sorted(ret)
