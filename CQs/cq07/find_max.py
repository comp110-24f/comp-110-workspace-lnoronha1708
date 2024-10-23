__author__ = "730766709"


def find_and_remove_max(input: list[int]) -> int:
    """find, return, remove largest number in list"""
    if len(input) == 0:
        return -1  # returns -1 if list is empty
    idx: int = 0
    max: int = input[idx]

    # find max val
    while idx < len(input):
        if input[idx] > max:
            max = input[idx]
        idx += 1

    # reset index to find and remove max val
    idx = 0
    while idx < len(input):
        if max == input[idx]:
            input.pop(idx)
            idx -= 1  # if remove value, it will possibly skip
        idx += 1
    return max
