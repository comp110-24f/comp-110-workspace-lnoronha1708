"""Summing the elements of a list using different loops"""

__author__ = "730766709"


def w_sum(vals: list[float]) -> float:
    """returns sum of elements with while loop"""
    idx: int = 0
    sum: float = 0
    while idx < len(vals):
        sum += vals[idx]
        idx += 1
    return sum


def f_sum(vals1: list[float]) -> float:
    """returns sum of elements with for in loop"""
    sum: float = 0
    for elem in vals1:
        sum += elem
    return sum


def f_range_sum(vals2: list[float]) -> float:
    """returns sum of elements with range and for in loop"""
    sum: float = 0
    for elem in range(0, len(vals2)):
        sum += vals2[elem]
    return sum
