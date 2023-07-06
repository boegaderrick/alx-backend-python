#!/usr/bin/env python3
"""This module contains a function that returns a tuple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
        This function takes a string and either an int or float and returns
        a tuple containing the string and a square of the int or float
    """
    return (k, v * v)
