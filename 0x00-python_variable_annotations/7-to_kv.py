#!/usr/bin/env python3
"""
Complex types - string and int/float to tuple
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Takes a string 'k' and an int or float 'v', returns a tuple
    where the first element is 'k', and the second element is the square of
    'v' as a float.
    """
    return (k, float(v ** 2))
