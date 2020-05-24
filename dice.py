def dice(sides=6, rolls=10):
    """Rolling dice of x sides y times."""
    import random
    dice_sides = [x for x in range(1, sides + 1)]
    dice_rolls = []
    for y in range(rolls):
        roll_output = random.choice(dice_sides)
        dice_rolls.append(roll_output)
    return dice_rolls


print(dice())
# print(dice(10))
# print(dice(15))
