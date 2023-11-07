""" Programm for declare array of numbers and calculating average of it """


def calculate_average(numbers):
    """Method of calculating the average of numbers"""
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    return average


nums = [10, 15, 20]
result = calculate_average(nums)
print("The average is:", result)
