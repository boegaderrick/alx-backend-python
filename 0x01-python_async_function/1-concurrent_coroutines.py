#!/usr/bin/env python3
"""This module contains an asyncronous function"""
import asyncio
from typing import Callable, List

wait_random: Callable = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
        This function calls a co-routine multiple times. A list of the
        returns of the co-routine calls is sorted and returned
    """
    ret = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(ret)
