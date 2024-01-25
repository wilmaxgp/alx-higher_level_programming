#!/usr/bin/python3
"""
Module: 101-square
Class: Square
Defines a square with private size and position attributes.
"""

class Square:
    """
    Class: Square
    Defines a square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance.

        Parameters:
        - size (int): The size of the square (optional, default is 0).
        - position (tuple): The position of the square (optional, default is (0, 0)).

        Raises:
        - TypeError: If size is not an integer or position is not a tuple of 2 positive integers.
        - ValueError: If size is less than 0 or position contains non-positive integers.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
        - int: The size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Setter method for the size attribute.

        Parameters:
        - value: The new value for the size attribute (must be an integer).

        Raises:
        - TypeError: If value is not an integer.
        - ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    @property
    def position(self):
        """
        Getter method for the position attribute.

        Returns:
        - tuple: The position of the square.
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Setter method for the position attribute.

        Parameters:
        - value (tuple): The new value for the position.

        Raises:
        - TypeError: If value is not a tuple of 2 positive integers.
        - ValueError: If value contains non-positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) for i in value) or any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
        - int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square with the character #, using the position attribute.

        If size is equal to 0, prints an empty line.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """
        Returns a string representation of the square.

        Returns:
        - str: A string representation of the square.
        """
        result = []
        for _ in range(self.__position[1]):
            result.append('')
        for _ in range(self.__size):
            result.append(' ' * self.__position[0] + '#' * self.__size)
        return '\n'.join(result)
