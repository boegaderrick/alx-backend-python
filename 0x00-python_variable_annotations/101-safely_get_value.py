#!/usr/bin/env python3
"""This module contains a function that returna a random value"""
from typing import Any, Mapping, TypeVar, Union


T = TypeVar('T')
alias = Union[T, None]
def safely_get_value(dct: Mapping, key: Any, default: alias = None) -> Union[Any, T]:
    """
        This function takes three parameters and determines a return value
        using the parameters passed on the parameters passed.
    """
    if key in dct:
        return dct[key]
    else:
        return default
