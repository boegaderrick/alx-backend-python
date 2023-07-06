#!/usr/bin/env python3
"""This module contains a function that returns a  list of tuples"""
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
        This function takes an iterable containing sequences and returns
        a list of tuples each containing a sequence from the iterable and
        its length.
    """
    return [(i, len(i)) for i in lst]
