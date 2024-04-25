def sum_average(number):
    if number < 1:
        return "Please enter a positive integer greater than 0."
    
    total = number * (number + 1) // 2
    average = total / number
    
    return total, average

def check(candidate):
    assert sum_average(10)==(55, 5.5)
    assert sum_average(15)==(120, 8.0)
    assert sum_average(20)==(210, 10.5)

check(sum_average)