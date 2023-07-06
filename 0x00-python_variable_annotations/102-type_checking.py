#!/usr/bin/env python3
"""This module containes a function that returns a list"""
from typing import Any, List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """This function takes 2 parameters and returns a list"""
    zoomed_in: List[Any] = [
        item for item in lst
        for i in range(int(factor))
    ]
    return zoomed_in


tup = (12, 72, 91)

zoom_2x = zoom_array(tup)

zoom_3x = zoom_array(tup, 3)
