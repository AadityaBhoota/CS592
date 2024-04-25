def even_Power_Sum(n): 
    sum = 0
    for i in range(1, n*2+1):
        if i % 2 == 0:
            sum += i**5
    return sum

# Test cases




def check(candidate):
    assert even_Power_Sum(2) == 1056
    assert even_Power_Sum(3) == 8832
    assert even_Power_Sum(1) == 32

check(even_Power_Sum)