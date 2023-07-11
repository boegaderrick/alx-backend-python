#!/usr/bin/env python3
"""This module contains an asyncronous generator"""
from asyncio import sleep
from random import uniform
from typing import Generator


# async def async_generator() -> AsyncGenerator[float, None]:
async def async_generator() -> Generator[float, None, None]:
    """
        This function loops ten times and in each iteration generates random
        floats between 0 and 10 and yields in intervals of one second.
    """
    for i in range(10):
        await sleep(1)
        yield uniform(0, 10)
