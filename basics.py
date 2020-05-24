def mean(x):
    """Find the mean of an input of numbers"""
    x_mean = sum(x)/len(x)
    return x_mean

def error(x):
    """Chooses a number from a list of numbers"""
    import random
    x_error = random.choice(x)
    return x_error
