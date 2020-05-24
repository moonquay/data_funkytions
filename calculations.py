from basics import mean, error

my_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
print("Starting with this list of numbers: " + str(my_list))
print("The mean is: " + str(mean(my_list)))
print("The error is: " + str(error(my_list, mean(my_list))))

