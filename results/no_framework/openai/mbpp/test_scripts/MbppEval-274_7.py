import math

def even_binomial_Coeff_Sum(n):
    total_sum = 0
    for i in range(n+1):
        coeff = math.comb(n, i)
        if i % 2 == 0:
            total_sum += coeff
    return total_sum

# Test cases




def check(candidate):
    assert even_binomial_Coeff_Sum(4) == 8
    assert even_binomial_Coeff_Sum(6) == 32
    assert even_binomial_Coeff_Sum(2) == 2

check(even_binomial_Coeff_Sum)