def sum_odd(n): 
    result = 0
    
    for i in range(1, n+1):
        if i % 2 != 0:  # Check if the number is odd
            result += i
    
    return result

def check(candidate):
    assert sum_in_range(2,5) == 8
    assert sum_in_range(5,7) == 12
    assert sum_in_range(7,13) == 40

check(sum_odd)