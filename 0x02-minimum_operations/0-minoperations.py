#!/usr/bin/python3
"""minimum operation"""


def minOperations(n):
    """compute minimum number of operation needed to copy and paste a srting"""
    if n <= 1:
        return 0
    for val in range(2, n + 1):
        if n % val == 0:
            return minOperations(n // val) + val
    return n
