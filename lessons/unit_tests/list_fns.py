"""testing different functions"""


def get_first(input: list[str]) -> str:
    """returns first element in list"""
    return input[0]


def remove_first(input: list[str]) -> None:
    """removes first element off list"""
    input.pop(0)


def get_an_remove_first(input: list[str]) -> str:
    """ "returns first element and pops it off"""
    first: str = input[0]
    input.pop(0)
    return first
