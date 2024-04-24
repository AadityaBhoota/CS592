def even_Power_Sum(n): 
    sum = 0
    start = 2
    
    for _ in range(n):
        sum += pow(start, 5)
        start += 2
    
    return sum

# Test cases




def check(candidate):
    assert even_Power_Sum(2) == 1056
    assert even_Power_Sum(3) == 8832
    assert even_Power_Sum(1) == 32

check(even_Power_Sum)