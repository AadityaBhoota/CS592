import math

def even_binomial_Coeff_Sum(n):
    total_sum = 0
    for k in range(0, n+1, 2):
        binomial_coeff = math.comb(n, k)
        total_sum += binomial_coeff
    return total_sum

def check(candidate):
    assert even_binomial_Coeff_Sum(4) == 8
    assert even_binomial_Coeff_Sum(6) == 32
    assert even_binomial_Coeff_Sum(2) == 2

check(even_binomial_Coeff_Sum)