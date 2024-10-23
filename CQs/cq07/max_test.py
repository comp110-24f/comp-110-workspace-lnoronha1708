__author__ = "730766709"

from find_max import find_and_remove_max


def test1_find_and_remove_max() -> None:
    input: list[int] = [1, 2, 3, 4]
    assert find_and_remove_max(input) == 4


def test2_find_and_remove_max() -> None:
    input: list[int] = [1, 2, 3, 4]
    find_and_remove_max(input)
    assert input == [1, 2, 3]


def test3_find_and_remove_max() -> None:
    input: list[int] = []
    assert find_and_remove_max(input) == -1
