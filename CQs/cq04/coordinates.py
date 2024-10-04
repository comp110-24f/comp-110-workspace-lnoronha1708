"""Pratice importing functions from dif. files (coordinates)"""

__author__ = "730766709"


def get_coords(xs: str, ys: str) -> None:
    """prints formatted pairs of characters"""
    i: int = 0
    while i < len(xs):
        j: int = 0
        while j < len(ys):
            print("(" + xs[i] + "," + ys[j] + ")")
            j = j + 1
        i = i + 1
