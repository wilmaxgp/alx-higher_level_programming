#!/usr/bin/python3
"""
Module: 1-square
Class: Square
Defines a square with a private size attribute.
"""

class Square:
    """
    Class: Square
    Defines a square.
    """

    def __init__(self, size):
        """
        Initializes a new Square instance.

        Parameters:
        - size (int): The size of the square.

        Note: No type/value verification is performed.
        """
        self.__size = size
