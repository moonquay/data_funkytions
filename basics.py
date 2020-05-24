def mean(x):
    """Find the mean of an input of numbers"""
    x_mean = sum(x)/len(x)
    return x_mean

def error(list, y):
    """Subtracts an input value from a list of numbers"""
    y_errors = [z - y for z in list]
    return y_errors
