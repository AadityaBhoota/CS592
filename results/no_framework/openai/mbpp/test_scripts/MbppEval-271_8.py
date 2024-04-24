def even_Power_Sum(n):
    sum_of_even_powers = sum([(2*i)**5 for i in range(1, n+1)])
    return sum_of_even_powers

# Testing the function with given examples




def check(candidate):
    assert even_Power_Sum(2) == 1056
    assert even_Power_Sum(3) == 8832
    assert even_Power_Sum(1) == 32

check(even_Power_Sum)