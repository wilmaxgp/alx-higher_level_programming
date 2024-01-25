#!/usr/bin/python3
"""
Module: 102-square
Class: Square
Defines a square with private size attribute and comparators based on area.
"""

class Square:
    """
    Class: Square
    Defines a square.
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance.

        Parameters:
        - size: The size of the square (must be a number).
        """
        self.size = size

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
        - int or float: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Parameters:
        - value: The new value for the size attribute (must be a number).

        Raises:
        - TypeError: If value is not a number (float or integer).
        - ValueError: If value is less than 0.
        """
        if not isinstance(value, (float, int)):
            raise TypeError("size must be a number")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
        - int or float: The area of the square.
        """
        return self.__size ** 2

    def __eq__(self, other):
        """
        Equality comparator based on the square area.

        Parameters:
        - other: The other square to compare.

        Returns:
        - bool: True if the areas are equal, False otherwise.
        """
        return self.area() == other.area()

    def __ne__(self, other):
        """
        Inequality comparator based on the square area.

        Parameters:
        - other: The other square to compare.

        Returns:
        - bool: True if the areas are not equal, False otherwise.
        """
        return self.area() != other.area()

    def __lt__(self, other):
        """
        Less than comparator based on the square area.

        Parameters:
        - other: The other square to compare.

        Returns:
        - bool: True if the area is less than the other square's area, False otherwise.
        """
        return self.area() < other.area()

    def __le__(self, other):
        """
        Less than or equal to comparator based on the square area.

        Parameters:
        - other: The other square to compare.

        Returns:
        - bool: True if the area is less than or equal to the other square's area, False otherwise.
        """
        return self.area() <= other.area()

    def __gt__(self, other):
        """
        Greater than comparator based on the square area.

        Parameters:
        - other: The other square to compare.

        Returns:
        - bool: True if the area is greater than the other square's area, False otherwise.
        """
        return self.area() > other.area()

    def __ge__(self, other):
        """
        Greater than or equal to comparator based on the square area.

        Parameters:
        - other: The other square to compare.

        Returns:
        - bool: True if the area is greater than or equal to the other square's area, False otherwise.
        """
        return self.area() >= other.area()
