#!/usr/bin/env python3
"""This module contains a function that calls an coroutine"""
from asyncio import run
from time import perf_counter
from typing import Callable

wait_n: Callable = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
        This function calls a coroutine and measures the time the
        coroutine takes to complete executing and returns it
    """
    start: float = perf_counter()
    run(wait_n(n, max_delay))
    return (perf_counter() - start) / n
