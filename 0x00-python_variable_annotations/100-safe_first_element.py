#!/usr/bin/env python3
"""This module contains a function that returns a value or nothing"""
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
        This function takes a sequence with 'None' as the default value,
        if the caller doesn't pass a parameter to override the default
        value 'None' is returned, else the first item of the sequence
        is returned.
    """
    if lst:
        return lst[0]
    else:
        return None
