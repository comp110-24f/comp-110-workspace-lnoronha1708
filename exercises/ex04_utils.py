"""list Utility Functions - 4 dif. functions"""

__author__ = "730766709"


def all(list1: list[int], val1: int) -> bool:
    """returns bool if val1 is same value as all ints in list"""
    idx: int = 0
    count: int = 0
    while idx < len(list1):
        if list1[idx] == val1:
            count += 1
        idx += 1
    if count == len(list1):
        return True
    else:
        return False


# this one went pretty smoothly! :)


def max(list2: list[int]) -> int:
    """returns largest int in list"""
    if len(list2) == 0:
        raise ValueError("max() arg is an empty List")
    idx: int = 0
    val: int = list2[idx]
    while idx < len(list2):
        if list2[idx] > val:
            val = list2[idx]
        idx += 1
    return val


# tried to do list2[idx+1], but then out of range, figured it out!


def is_equal(list1: list[int], list2: list[int]) -> bool:
    idx: int = 0
    while idx < len(list1) and idx < len(list2):
        if list1[idx] == list2[idx]:
            idx += 1
        else:
            return False
    return True


# not sure if i need to return False if len is dif? rn it return True when not same len


def extend(list1: list[int], list2: list[int]) -> None:
    """add 2nd list to 1st list"""
    idx: int = 0
    while idx < len(list2):
        list1.append(list2[idx])
        idx += 1
    return None


# when i add b, it includes the brackets []
# made the while loop to ru through each index and value, fixed it!
