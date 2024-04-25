def sum_average(number):
    total_sum = 0
    average = 0

    total_sum = (number * (number + 1)) // 2
    average = total_sum / number

    return total_sum, average

def check(candidate):
    assert sum_average(10)==(55, 5.5)
    assert sum_average(15)==(120, 8.0)
    assert sum_average(20)==(210, 10.5)

check(sum_average)