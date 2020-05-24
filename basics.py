def mean(x):
    """Find the mean of an input of numbers"""
    x_mean = sum(x)/len(x)
    return x_mean
    # print('The mean is: ' + str(x_mean))

def error(list, y):
    """Subtracts an input value from a list of numbers"""
    y_errors = [z - y for z in list]
    return y_errors
    # print('The error is: ' + str(y_errors))