"""Pratice importing functions from dif. files (concatenation)"""

__author__ = "730766709"


def concat(val1: str, val2: str) -> str:
    return val1 + val2


if __name__ == "__main__":
    word1: str = "happy"
    word2: str = "tuesday"
    print(concat(word1, word2))