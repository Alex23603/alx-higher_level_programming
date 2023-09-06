#!/usr/bin/python3
# 6-max_integer_test.py
"""Unittests for max_integer([..])."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Define unittests for max_integer([..])."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [1, 2, 4, 3]
        self.assertEqual(max_integer(unordered), 4)

    def test_max_at_begginning(self):
        """Test a list with a beginning max value."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_element_list(self):
        """Test a list with a single element."""
        one_element = [7]
        self.assertEqual(max_integer(one_element), 7)

    def test_floats(self):
        """Test a list of floats."""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_ints_and_floats(self):
        """Test a list of ints and floats."""
        ints_and_floats = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(ints_and_floats), 15.5)

    def test_string(self):
        """Test a string."""
        string = "Brennan"
        self.assertEqual(max_integer(string), 'r')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Brennan", "is", "my", "name"]
        self.assertEqual(max_integer(strings), "name")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

if __name__ == '__main__':
    unittest.main()


+++++++++++++++++++++++++++++++++++

100-matrix_mul.txt

# 100-matrix_mul.txt

============================
How to Use 100-matrix_mul.py
============================

This module defines a matrix multiplication function ``matrix_mul(m_a, m_b)``.

Usage
=====
``matrix_mul(...)`` returns a new matrix representing the multiplication of
``m_a`` by ``m_b``.

::

    >>> matrix_mul = __import__('100-matrix_mul').matrix_mul
    >>> m_a = [
    ... [1, 2],
    ... [3, 4],
    ... ]
    >>> m_b = m_a
    >>> print(matrix_mul(m_a, m_b))
    [[7, 10], [15, 22]]

::

    >>> m_a = [[1, 2]]
    >>> m_b = [
    ... [3, 4],
    ... [5, 6]
    ... ]
    >>> print(matrix_mul(m_a, m_b))
    [[13, 16]]

The function also works with floating-point numbers.

::

    >>> m_a = [
    ... [1.2, 5.5, 6.2],
    ... [4.66, 12.3, -9.2]
    ... ]
    >>> m_b = [
    ... [5.0, 3.3],
    ... [-2.9, 4.4],
    ... [7.2, 4.4]
    ... ]
    >>> print(matrix_mul(m_a, m_b))
    [[34.69, 55.44000000000001], [-78.61, 29.018000000000008]]

Integers and floats can be combined.

::

    >>> m_a = [
    ... [1, 2.2, 3.3, 4],
    ... [5, 6, 7, 8.8],
    ... ]
    >>> m_b = [
    ... [1.1, 2, 3.3],
    ... [4.0, 5.5, 6],
    ... [7, 8, 9],
    ... [10.01, 11, 12.3]
    ... ]
    >>> print(matrix_mul(m_a, m_b))
    [[73.03999999999999, 84.5, 95.4], [166.58800000000002, 195.8, 223.74]]

A minimum of two arguments must be provided. Otherwise, a TypeError is raised.

::

    >>> print(matrix_mul()) # doctest: +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
    TypeError: matrix_mul() missing 2 required positional arguments: 
    'm_a' and 'm_b'

::

    >>> print(matrix_mul()) # doctest: +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
    TypeError: matrix_mul() missing 2 required positional arguments: 
    'm_a' and 'm_b'

ValueErrors
===========

If two matrices cannot be multiplied (ie. the row count of ``m_a`` is not
equal to the column count in ``m_b``), a ValueError is raised.

::

    >>> m_a = [
    ... [1, 2],
    ... [3, 4],
    ... ]
    >>> m_b = [
    ... [1, 2],
    ... [2, 3],
    ... [4, 5]
    ... ]
    >>> print(matrix_mul(m_a, m_b))
    Traceback (most recent call last):
    ValueError: m_a and m_b can't be multiplied


The parameters ``m_a`` and ``m_b`` cannot be empty. Otherwise, a ValueError
is raised.

::

    >>> print(matrix_mul([], [[1, 2]]))
    Traceback (most recent call last):
    ValueError: m_a can't be empty

::

    >>> print(matrix_mul([[1, 2]], [[]]))
    Traceback (most recent call last):
    ValueError: m_b can't be empty

::

    >>> print(matrix_mul([[]], []))
    Traceback (most recent call last):
    ValueError: m_a can't be empty

Invalid Matrices
================

The parameters ``m_a`` and ``m_b`` must be lists. If either parameter is
not a list, a TypeError is raised.

::

    >>> print(matrix_mul("not a list", [[1, 2]]))
    Traceback (most recent call last):
    TypeError: m_a must be a list

::

    >>> print(matrix_mul([[1, 2]], "also not a list"))
    Traceback (most recent call last):
    TypeError: m_b must be a list

::

    >>> print(matrix_mul("not a list", "also not a list"))
    Traceback (most recent call last):
    TypeError: m_a must be a list

::

    >>> print(matrix_mul(None, None))
    Traceback (most recent call last):
    TypeError: m_a must be a list

Not just any list - they *must* be lists of lists!

::

    >>> print(matrix_mul([1, 2], [[3, 4]]))
    Traceback (most recent call last):
    TypeError: m_a must be a list of lists

::

    >>> print(matrix_mul([[1, 2]], [3, 4]))
    Traceback (most recent call last):
    TypeError: m_b must be a list of lists

::

    >>> print(matrix_mul([1, 2], [3, 4]))
    Traceback (most recent call last):
    TypeError: m_a must be a list of lists

And not just any list of lists - they *must* be lists of lists containing
integers or floats!

::

    >>> print(matrix_mul([[1, "non-number"]], [[3, 4]]))
    Traceback (most recent call last):
    TypeError: m_a should contain only integers or floats

::

    >>> print(matrix_mul([[1, 2]], [[{"a": 1}, 8.8]]))
    Traceback (most recent call last):
    TypeError: m_b should contain only integers or floats

::

    >>> print(matrix_mul([[1, "non-number"]], [[{"a": 1}, 8.8]]))
    Traceback (most recent call last):
    TypeError: m_a should contain only integers or floats

Finally, the length of all rows in matrices ``m_a`` and ``m_b`` should be
equivalent. Otherwise, a TypeError is raised.

::

    >>> m_a = [
    ... [1, 2],
    ... [3, 4, 5]
    ... ]
    >>> m_b = [
    ... [1, 2],
    ... [3, 4]
    ... ]
    >>> print(matrix_mul(m_a, m_b))
    Traceback (most recent call last):
    TypeError: each row of m_a must should be of the same size

::

    >>> m_a = [
    ... [1, 2],
    ... [3, 4]
    ... ]
    >>> m_b = [
    ... [1, 2],
    ... [3, 4, 5]
    ... ]
    >>> print(matrix_mul(m_a, m_b))
    Traceback (most recent call last):
    TypeError: each row of m_b must should be of the same size

::

    >>> m_a = [
    ... [1, 2],
    ... [3, 4, 5]
    ... ]
    >>> m_b = m_a
    >>> print(matrix_mul(m_a, m_b))
    Traceback (most recent call last):
    TypeError: each row of m_a must should be of the same size
