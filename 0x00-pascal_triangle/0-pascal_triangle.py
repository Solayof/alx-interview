#!/usr/bin/python3
"""Function that n level pascal triangle"""


def pascal_triangle(n):
    """function that return list of n levels of pascal triangle
    """
    if n <= 0:
        return []

    lists = [[1]]
    n_row = [1]
    for _ in range(n - 1):
        n_row = [1]
        r_row = lists[-1]
        n_row += [sum(value) for value in zip(r_row, r_row[1:])]
        n_row.append(1)
        lists.append(n_row)

    return lists
