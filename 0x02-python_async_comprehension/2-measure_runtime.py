#!/usr/bin/env python3
"""This module contains a coroutine"""

from asyncio import gather
from time import perf_counter
from typing import Callable

async_comprehension: Callable = __import__(
                                '1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
        This function calls a coroutine four times then measures the execution
        period and returns it to the caller.
    """
    start: float = perf_counter()
    await gather(*[async_comprehension() for _ in range(4)])
    return perf_counter() - start
