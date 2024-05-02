#!/usr/bin/env python3
"""
Duck typing - first element of a sequence
"""


from typing import Sequence, Any, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """
    Returns the first element of a sequence if it is non-empty.
    If the sequence is empty, returns None.

    Args:
    lst (Sequence[Any]): A sequence of any type.

    Returns:
    Optional[Any]: The first element of the sequence, or None if the sequence
    is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
