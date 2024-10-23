""""List Utility Functions Ex 05"""

__author__ = "730766709"


def only_evens(list1: list[int]) -> list[int]:
    """Returns new list of values in old list that were even"""
    idx: int = 0
    evens_list: list[int] = []
    while idx < len(list1):
        if list1[idx] % 2 == 0:
            evens_list.append(list1[idx])
        idx += 1
    return evens_list


# was not working for  bit, but it was because return was in while loop oops!


def sub(a_list: list[int], start_idx: int, end_idx: int) -> list[int]:
    """Generates a subset list of input list"""
    idx: int = start_idx
    sub_list: list[int] = []
    while idx < len(a_list):
        if idx < 0 or idx > len(a_list):
            return a_list
        elif len(a_list) == 0 or start_idx > len(a_list) or end_idx <= 0:
            return []
        elif idx < end_idx:
            sub_list.append(a_list[idx])
        idx += 1
    return sub_list


# took a little to get it to return a_list if idx out of range
# i should read instructions better, so it doesn't take so long


def add_at_index(list_1: list[int], element: int, idx_val: int) -> None:
    """Modifies input list to place element at given index"""
    if idx_val < 0 or idx_val > len(list_1):
        raise IndexError("Index is out of bounds for the input list")
    list_1.append(0)  # dummy int as a space to move list
    idx: int = len(list_1) - 1  # idx is last int in list
    while (
        idx > idx_val
    ):  # index must be larger than idx_val bc only shifting what greater
        list_1[idx] = list_1[idx - 1]  # old list shift
        idx -= 1  # move backwards
    list_1[idx_val] = element  # once reach idx_val then can replace/insert


# this one was hard, I didn't understand the shift until I saw diagram on Ed
