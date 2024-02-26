#!/usr/bin/python3
"""
This module contains a function print_square.
"""


def print_square(size):
    """
    Print a square of '#' characters with the given size.

    Args:
        size (int): Size length of the square.

    Raises:
        TypeError: If size is not an integer or if size is a float less than 0.
        ValueError: If size is less than 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)


if __name__ == "__main__":
    print_square(4)
