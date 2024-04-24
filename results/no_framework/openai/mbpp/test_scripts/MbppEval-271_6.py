def even_Power_Sum(n):
    total_sum = sum([(2*i)**5 for i in range(1, n+1)])
    return total_sum

# Test the function with example cases




def check(candidate):
    assert even_Power_Sum(2) == 1056
    assert even_Power_Sum(3) == 8832
    assert even_Power_Sum(1) == 32

check(even_Power_Sum)