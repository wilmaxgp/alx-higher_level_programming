#!/usr/bin/python3
"""
This module contains a function lazy_matrix_mul.
"""
import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy.

    Args:
        m_a (list of list): First matrix.
        m_b (list of list): Second matrix.

    Returns:
        np.ndarray: Result of matrix multiplication.

    Raises:
        TypeError: If m_a or m_b is not a list or not a list of lists,
            or if any element in m_a or m_b is not an integer or float,
            or if each row of m_a or m_b is not of the same size.
        ValueError: If m_a or m_b is empty, or if m_a and m_b cannot be multiplied.
    """
    # Convert input matrices to NumPy arrays
    arr_a = np.array(m_a)
    arr_b = np.array(m_b)

    # Perform matrix multiplication using NumPy
    result = np.matmul(arr_a, arr_b)

    return result
