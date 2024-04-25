def sum_average(number):
    if number < 1:
        return None

    total_sum = number * (number + 1) // 2
    avg = total_sum / number
    
    return (total_sum, avg)

# Test cases




def check(candidate):
    assert sum_average(10)==(55, 5.5)
    assert sum_average(15)==(120, 8.0)
    assert sum_average(20)==(210, 10.5)

check(sum_average)