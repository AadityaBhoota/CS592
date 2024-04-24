def even_binomial_Coeff_Sum(n):
    def binomial_coefficient(n, k):
        return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))

    sum_even = 0
    for k in range(0, n + 1, 2):
        sum_even += binomial_coefficient(n, k)

    return sum_even

# Test cases




def check(candidate):
    assert even_binomial_Coeff_Sum(4) == 8
    assert even_binomial_Coeff_Sum(6) == 32
    assert even_binomial_Coeff_Sum(2) == 2

check(even_binomial_Coeff_Sum)