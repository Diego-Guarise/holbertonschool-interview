#!/usr/bin/python3
"""
In a text file, there is a single character H. Your text editor can
execute only two operations in this file: Copy All and Paste.
Given a number n, write a method that calculates the fewest number
of operations needed to result in exactly n H characters in the
file.
"""


def minOperations(n):
    """
    Prototype: def minOperations(n)
    Returns an integer
    If n is impossible to achieve, return 0
    """
    result = 0
    i = 2

    if isinstance(n, int) and n < 2:
        return 0

    while i <= n + 1:
        if n % i == 0:
            result += i
            n //= i
            i = 2
        else:
            i += 1

    return result
