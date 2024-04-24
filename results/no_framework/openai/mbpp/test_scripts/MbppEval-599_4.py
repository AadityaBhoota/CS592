def sum_average(number):
    # Calculate the sum of the first n natural numbers
    total_sum = number * (number + 1) // 2
    
    # Calculate the average of the first n natural numbers
    average = total_sum / number
    
    return total_sum, average

# Test cases




def check(candidate):
    assert sum_average(10)==(55, 5.5)
    assert sum_average(15)==(120, 8.0)
    assert sum_average(20)==(210, 10.5)

check(sum_average)