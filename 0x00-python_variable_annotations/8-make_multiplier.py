#!/usr/bin/env python3
"""This module contains a function that returns a nested function"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """This function takes a float and returns a nested function"""
    def func(fl: float) -> float:
        """
            This function takes a float and multiplies it by another float
            then returns the product
        """
        return fl * multiplier

    return func
