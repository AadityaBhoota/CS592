def sum_average(number):
    """
    Write a function to find the sum and average of the first n natural numbers.

    Args:
        number (int): The number of natural numbers to consider.

    Returns:
        tuple: A tuple containing the sum and average of the first n natural numbers.
    """
    total_sum = (number * (number + 1)) // 2
    average = total_sum / number
    return (total_sum, average)

def check(candidate):
    assert sum_average(10)==(55, 5.5)
    assert sum_average(15)==(120, 8.0)
    assert sum_average(20)==(210, 10.5)

check(sum_average)