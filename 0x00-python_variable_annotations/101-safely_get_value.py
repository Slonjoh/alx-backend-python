#!/usr/bin/env python3
"""
More involved type annotations
"""


from typing import Mapping, Any, TypeVar, Union


T = TypeVar("T")  # Declare a type variable


def safely_get_value(
    dct: Mapping,
    key: Any,
    default: Union[T, None] = None
) -> Union[Any, T]:
    """
    Returns the value from the dictionary if the key is found.
    Otherwise, returns the default value provided or None.

    Args:
    dct (Mapping[Any, Any]): The dictionary or mapping to search.
    key (Any): The key to look for in the dictionary.
    default (Union[T, None], optional): The default value to return if the
    key is not found. Defaults to None.

    Returns:
    Union[Any, T]: The value associated with the key, or the default if the
    key is not found.
    """
    if key in dct:
        return dct[key]
    else:
        return default
