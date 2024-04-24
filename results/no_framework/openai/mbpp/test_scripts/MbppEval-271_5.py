def even_Power_Sum(n):
    if n <= 0:
        return 0
    
    sum = 0
    count = 0
    i = 2
    
    while count < n:
        sum += i**5
        i += 2
        count += 1
    
    return sum

# Test cases




def check(candidate):
    assert even_Power_Sum(2) == 1056
    assert even_Power_Sum(3) == 8832
    assert even_Power_Sum(1) == 32

check(even_Power_Sum)