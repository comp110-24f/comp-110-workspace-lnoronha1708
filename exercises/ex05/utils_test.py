""""List Utility Functions Test Ex 05"""

__author__ = "730766709"

from utils import only_evens, sub, add_at_index

import pytest


def test_1_only_evens() -> None:
    """Tests if returns new list of even values from old list"""
    input: list[int] = [1, 2, 3]
    assert only_evens(input) == [2]


def test_2_only_evens() -> None:
    """Tests how only_evens function mutates input"""
    input: list[int] = [1, 5, 3]
    assert only_evens(input) == []


def test_3_only_evens() -> None:
    """Edge case for only_evens, if empty list input"""
    input: list[int] = []
    assert only_evens(input) == []


def test_1_sub() -> None:
    """Tests if returns sub list based on start and end idx"""
    input: list[int] = [10, 20, 30, 40]
    assert sub(input, 1, 3) == [20, 30]


def test_2_sub() -> None:
    """Tests how sub function mutates input"""
    input: list[int] = [1, 2, 3, 4]
    assert sub(input, -1, 5) == [1, 2, 3, 4]


def test_3_sub() -> None:
    """Edge case test for sub, if empty list"""
    input: list[int] = []
    assert sub(input, 2, 4) == []


def test_1_add_at_index() -> None:
    """Tests what add_at_index returns"""
    input: list[int] = [1, 2, 3, 5]
    assert add_at_index(input, 4, 3) == None


def test_2_add_at_index() -> None:
    """Tests how add_at_index mutates lists"""
    input: list[int] = [1, 2, 3, 5]
    add_at_index(input, 4, 3)
    assert input == [1, 2, 3, 4, 5]


def test_3_add_at_index() -> None:
    """Tests that add_at_index raises IndexError for invalid index"""
    # your object to pass to add_at_index function
    input: list[int] = []
    with pytest.raises(IndexError):
        add_at_index(input, 1, 1)
        # an IndexError is raised for the case when the add_at_index is given an <index_to_insert_num>
        # that is greater than the length of our <list_object>
