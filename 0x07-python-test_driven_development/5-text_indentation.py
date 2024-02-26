#!/usr/bin/python3
"""
This module contains a function text_indentation.
"""


def text_indentation(text):
    """
    Print text with 2 new lines after each '.', '?' and ':' character.

    Args:
        text (str): The input text.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in text:
        print(char, end="")
        if char in ['.', '?', ':']:
            print("\n\n", end="")
