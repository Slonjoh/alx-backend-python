#!/usr/bin/env python3
"""
Let's duck type an iterable object
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    Takes an iterable of sequences and returns a list of tuples.
    Each tuple contains a sequence and its length.

    Args:
    lst (Iterable[Sequence]): An iterable containing sequences.

    Returns:
    List[Tuple[Sequence, int]]: A list of tuples, where each tuple contains
    a sequence and its length.
    """
    return [(i, len(i)) for i in lst]
