from collections import defaultdict

def dice(sides=6, rolls=10):
    """Rolling dice of x sides y times."""
    import random
    dice_sides = [x for x in range(1, sides + 1)]
    dice_rolls = []
    for y in range(rolls):
        roll_output = random.choice(dice_sides)
        dice_rolls.append(roll_output)
    return dice_rolls

dice_rolls = dice()

roll_counts = defaultdict(int)
for roll in dice_rolls:
    roll_counts[roll] += 1

# print(roll_counts)
# print(roll_counts[6])

# print(dice(10))
# print(dice(15))
