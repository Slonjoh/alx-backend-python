#!/usr/bin/env python3
"""
Type Checking
"""


from typing import List, Tuple


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """
    Takes a tuple 'lst' and returns a list where each item from the
    tuple is repeated 'factor' times.

    Args:
    lst (Tuple): The input tuple to be zoomed.
    factor (int, optional): The repetition factor. Default is 2.

    Returns:
    List: A list with each item from the input tuple repeated 'factor' times.
    """
    zoomed_in: List = [
        item for item in lst
        for _ in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)  # Ensure the input is a tuple

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3)  # The factor should be an integer
