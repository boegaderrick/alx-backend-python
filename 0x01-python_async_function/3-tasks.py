#!/usr/bin/env python3
"""This module contains a funtion that returns a Task object"""
from asyncio import create_task, Task
from typing import Callable

wait_random: Callable = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> Task:
    """This function creates and returns a Task object"""
    return create_task(wait_random(max_delay))
