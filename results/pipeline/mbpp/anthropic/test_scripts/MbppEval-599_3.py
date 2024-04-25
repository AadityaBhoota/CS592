def sum_average(number):
    total = 0
    for i in range(1, number+1):
        total += i
    average = total / number
    return (total, average)

def check(candidate):
    assert sum_average(10)==(55, 5.5)
    assert sum_average(15)==(120, 8.0)
    assert sum_average(20)==(210, 10.5)

check(sum_average)