import math

def even_binomial_Coeff_Sum(n):
    result = 0
    for k in range(n+1):
        binom_coeff = math.comb(n, k)
        if k % 2 == 0:
            result += binom_coeff
    return result

# Test the function




def check(candidate):
    assert even_binomial_Coeff_Sum(4) == 8
    assert even_binomial_Coeff_Sum(6) == 32
    assert even_binomial_Coeff_Sum(2) == 2

check(even_binomial_Coeff_Sum)