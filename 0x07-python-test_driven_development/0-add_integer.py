#!/usr/bin/python3
"""
This module defines a function that adds two integers.

Prototype: def add_integer(a, b=98):
- a and b must be integers or floats, otherwise raise a TypeError exception with the message:
    "a must be an integer" or "b must be an integer".
- a and b must be first casted to integers if they are float.
- Returns an integer: the addition of a and b.
You are not allowed to import any module.
"""

def add_integer(a, b=98):
    """
    Adds two integers.

    Parameters:
    - a: an integer or float.
    - b: an integer or float (default is 98).

    Returns:
    - An integer: the addition of a and b.
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return int(a) + int(b)

# Example usage
if __name__ == "__main__":
    print(add_integer(1, 2))
    print(add_integer(100, -2))
    print(add_integer(2))
    print(add_integer(100.3, -2))

    try:
        print(add_integer(4, "School"))
    except Exception as e:
        print(e)

    try:
        print(add_integer(None))
    except Exception as e:
        print(e)
