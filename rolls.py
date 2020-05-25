
def roll_probability(sides=6, rolls=10, target=6, number_of_targets=3, simulations=1000):
    """Determine the probability of rolling 'number_of_target' rolls of 'target' number
    in 'rolls' rolls using a 'sides'-sided dice, simulated 'simulations' times."""
    from dice import dice
    from collections import defaultdict
    succesful_sim = 0
    i = 0
    while i < simulations:
        roll_list = dice(sides, rolls)
        roll_counts = defaultdict(int)
        for roll in roll_list:
            roll_counts[roll] += 1
        num_target_rolls = roll_counts[target]
        if num_target_rolls >= number_of_targets:
            succesful_sim += 1
        i += 1
    # print(succesful_sim)
    probability = succesful_sim / simulations
    print(str(probability * 100) + '% chance of a ' + str(sides) + '-sided die rolling a total of ' + str(number_of_targets) + ' "' + str(target) + '"s over ' + str(rolls) + ' rolls.')

roll_probability(sides=6, rolls=10, target=6, number_of_targets=7, simulations=5000)
roll_probability(sides=250, rolls=198, target=15, number_of_targets=3, simulations=5000)
