def mean(x: list):
    """Calculates the arithmetic mean of an input of numbers"""
    x_mean = sum(x)/len(x)
    return x_mean
    # print('The mean is: ' + str(x_mean))

def error(list, y):
    """Subtracts an input value from a list of numbers"""
    y_errors = [z - y for z in list]
    return y_errors
    # print('The error is: ' + str(y_errors))

def variance(data: list) -> float:
    """
    Calculates the variance of a list of numeric values
    :param data: list of numeric values
    :return: float
    """
    data_mean = mean(data)
    sum_of_squares = sum((i - data_mean)**2 for i in data)
    return sum_of_squares

def std_dev(data: list, deg_of_freedom=1) -> float:
    """
    Calculates the standard deviation allowing for degrees of freedom
    :param data: list of numeric values
    :param deg_of_freedom: Degrees of freedom, set as 0 to compute without sample
    :return: float
    """
    sum_of_squares = variance(data)
    pvar = sum_of_squares / (len(data) - deg_of_freedom)
    sd = pvar ** 0.5
    return sd

def covariance(data_x: list, data_y: list) -> float:
    """
    Calculate covariance between two data lists of numeric variables
    :param data_x: list of numeric values
    :param data_y: list of numeric values
    :return: float
    """
    #assert len(data_x) == len(data_y)
    covar = 0.0
    x_mean = mean(data_x)
    y_mean = mean(data_y)
    for i in range(len(data_x)):
        covar += (data_x[i] - x_mean) * (data_y[i] - y_mean)
    return covar