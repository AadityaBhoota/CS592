def even_binomial_Coeff_Sum(n):
    total_sum = 0
    for k in range(n//2 + 1):
        coeff = math.comb(n, 2*k)
        total_sum += coeff
    return total_sum

# Test the function




def check(candidate):
    assert even_binomial_Coeff_Sum(4) == 8
    assert even_binomial_Coeff_Sum(6) == 32
    assert even_binomial_Coeff_Sum(2) == 2

check(even_binomial_Coeff_Sum)