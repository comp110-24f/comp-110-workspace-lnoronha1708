"""examples of dictionary syntax with ice cream shop order tallies"""

ice_cream: dict[str, int] = {
    "chocolate": 12,
    "vanilla": 8,
    "strawberry": 4,
}

for flavor in ice_cream:
    total_orders += ice_cream[flavor]
