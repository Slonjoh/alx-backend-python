#!/usr/bin/env python3
"""
Complex types - functions
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Takes a float 'multiplier' and returns a function that multiplies a float
    by 'multiplier'.
    """
    def multiply(x: float) -> float:
        """
        Multiplies a given float 'x' by 'multiplier'.

        Args:
        x (float): The float value to be multiplied.

        Returns:
        float: The result of 'x' multiplied by 'multiplier'.
        """
        return x * multiplier

    return multiply
