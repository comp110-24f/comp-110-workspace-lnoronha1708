"""2nd COMP110 exercise about tea!"""

__author__: str = "730766709"


def main_planner(guests: int) -> None:
    """Brings the tea party together!"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Teabags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )


# this section was very hard, especially printing cost


def tea_bags(people: int) -> int:
    """# of tea bags for guests"""
    return people * 2


def treats(people: int) -> int:
    """# of treats for guests"""
    return int(tea_bags(people) * 1.5)


# couldn't figure out how to switch from float to int, but got it


def cost(tea_count: int, treat_count: int) -> float:
    """cost of tea and treat for guests"""
    return (tea_count * 0.50) + (treat_count * 0.75)


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
