def sum_average(number):
    '''
    Write a function to find sum and average of first n natural numbers.

    Examples:
    sum_average(10) == (55, 5.5)
    sum_average(15) == (120, 8.0)
    sum_average(20) == (210, 10.5)
    '''
    # Calculate the sum of first n natural numbers
    total_sum = (number * (number + 1)) // 2

    # Calculate the average of first n natural numbers
    average = total_sum / number

    return (total_sum, average)

def check(candidate):
    assert sum_average(10)==(55, 5.5)
    assert sum_average(15)==(120, 8.0)
    assert sum_average(20)==(210, 10.5)

check(sum_average)