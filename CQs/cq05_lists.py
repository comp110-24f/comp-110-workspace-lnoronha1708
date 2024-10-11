"""Mutating functions."""

___author___ = "730766709"


def manual_append(list1: list[int], num_val: int) -> None:
    """mutate input, add int to list"""
    list1.append(num_val)
    return None


# this is so hard. TA is the goat


def double(list2: list[int]) -> None:
    """multiply list by 2"""
    index: int = 0
    while index < len(list2):
        list2[index] = list2[index] * 2  # could be *= 2
        index += 1
    return None


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)

print(list_1)
print(list_2)
