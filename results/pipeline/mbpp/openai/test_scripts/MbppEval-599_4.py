def sum_average(number):
    sum_numbers = number * (number + 1) // 2
    average = sum_numbers / number
    return (sum_numbers, average)

def check(candidate):
    assert sum_average(10)==(55, 5.5)
    assert sum_average(15)==(120, 8.0)
    assert sum_average(20)==(210, 10.5)

check(sum_average)