pets: list[str] = ["Louie", "Bo", "Bear"]

for elem in pets:
    print(f"Good boy, {elem}!")

# elem = name to refer to element
# pets = name of list


names: list[str] = ["Alyssa", "Janet", "Vrinda"]
for name in range(0, len(names)):
    print(str(name) + ": " + names[name])
