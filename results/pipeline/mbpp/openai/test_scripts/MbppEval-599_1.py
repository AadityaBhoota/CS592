def sum_average(number):
    sum = 0
    
    for i in range(1, number+1):
        sum += i
        
    average = sum / number
    
    return sum, average

# Test cases




def check(candidate):
    assert sum_average(10)==(55, 5.5)
    assert sum_average(15)==(120, 8.0)
    assert sum_average(20)==(210, 10.5)

check(sum_average)