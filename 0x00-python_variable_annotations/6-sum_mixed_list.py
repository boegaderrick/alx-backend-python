#!/usr/bin/env python3
"""This module contains a function that returns a sum"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
        This function takes a list of ints and floats and returns their sum
    """
    return sum(mxd_lst)
