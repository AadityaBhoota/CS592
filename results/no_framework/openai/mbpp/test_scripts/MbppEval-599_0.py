def sum_average(number):
    numbers = list(range(1, number + 1))
    total = sum(numbers)
    average = total / len(numbers)
    return total, average

# Test cases




def check(candidate):
    assert sum_average(10)==(55, 5.5)
    assert sum_average(15)==(120, 8.0)
    assert sum_average(20)==(210, 10.5)

check(sum_average)