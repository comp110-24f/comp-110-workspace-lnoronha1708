"""Practice with Dictionary Functions"""

__author__ = "730766709"


def invert(dict1: dict[str, str]) -> dict[str, str]:
    """inverts keys and values of dictionary"""
    dict2: dict[str, str] = {}
    list_vals: list[str] = []

    # keyerror if more than one of same key

    for key in dict1:
        if dict1[key] in list_vals:
            raise KeyError("More thn one of same key!")
        list_vals.append(dict1[key])

    # inverse keys and values
    for key in dict1:
        dict2[dict1[key]] = key
    return dict2


def favorite_colors(input: dict[str, str]) -> str:
    """Finds fav color through frequency in dictionary"""
    colors: list[str] = []  # contains all vals for colors from input
    for key in input:
        colors.append(input[key])
    color_dict: dict[str, int] = {
        "": 0,
    }  # begin w/ empty dict
    for color in colors:
        # if color exists, add, otherwise create and set = to 1
        if color in color_dict:
            color_dict[color] += 1
        else:
            color_dict[color] = 1
    fav_color: str = ""
    for key in reversed(color_dict):
        # reverse dict so first color most recent
        # check if value of color is larger, if yes that new fav color val
        if color_dict[key] > color_dict[fav_color]:
            fav_color = key
    return fav_color


def count(list1: list[str]) -> dict[str, int]:
    """count of number of times value in list"""
    dict_count: dict[str, int] = {}
    # if item exist in list add, otherwise create key and set = to 1
    for val in list1:
        if val in dict_count:
            dict_count[val] += 1
        else:
            dict_count[val] = 1
    return dict_count


def alphabetizer(alpha_list: list[str]) -> dict[str, list[str]]:
    """alphabetizes list into dict"""
    alpha_dict: dict[str, list[str]] = {}
    for word in alpha_list:
        # if word exist add, otherwise create key and set = to 1
        if word[0].lower() in alpha_dict:  # lower it to sort correctly
            alpha_dict[word[0].lower()].append(word)  # got help here
        else:
            alpha_dict[word[0].lower()] = [word]
    return alpha_dict


def update_attendance(attendance: dict[str, list[str]], day: str, student: str) -> None:
    """mutate and return dict with attendance updates"""
    # if day exist in attendance and student not in dict
    if day in attendance:
        if student not in attendance[day]:
            attendance[day].append(student)
        else:
            # if day does not exist, create key and add student
            attendance[day] = [student]
    return None
