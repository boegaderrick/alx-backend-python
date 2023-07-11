#!/usr/bin/env python3
"""This module contains coroutine that calls a coroutine"""

from typing import Callable, List

async_generator: Callable = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """This function demonstrates python's asyncronous comprehension"""
    return [i async for i in async_generator()]
