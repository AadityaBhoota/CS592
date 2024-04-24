def sum_average(number):
    # Calculate the sum of first 'number' natural numbers
    total_sum = number * (number + 1) // 2

    # Calculate the average
    average = total_sum / number

    return total_sum, average

# Test the function




def check(candidate):
    assert sum_average(10)==(55, 5.5)
    assert sum_average(15)==(120, 8.0)
    assert sum_average(20)==(210, 10.5)

check(sum_average)