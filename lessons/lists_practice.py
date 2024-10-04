my_numbers: list[float] = []  # literal version
my_numbers: list[float] = list()  # constructor version
print(my_numbers)

# # adding one item to list
my_numbers.append(1.5)
print(my_numbers)

# # make a list of numbers
game_points: list[int] = [102, 86, 94]
print(game_points)

print(game_points[2])
print(game_points[len(game_points) - 1])


# # changing value of an item by index
game_points[1] = 72
print(game_points)

# # can we change individual chars in  strings this way?
my_name: str = "leyla"
print(my_name)
# my_name[0] = "L" # didn't work, convert to list
name_as_list: list[str] = list(my_name)
print(name_as_list)
name_as_list[0] = "L"
print(name_as_list)

# # print length of game_points
print(len(game_points))

# # remove item from a list
game_points.pop(1)
print(game_points)

print(game_points[10])
