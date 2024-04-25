def sum_average(number):
    sum_of_numbers = (number * (number + 1)) // 2
    average_of_numbers = sum_of_numbers / number
    return sum_of_numbers, average_of_numbers

def check(candidate):
    assert sum_average(10)==(55, 5.5)
    assert sum_average(15)==(120, 8.0)
    assert sum_average(20)==(210, 10.5)

check(sum_average)