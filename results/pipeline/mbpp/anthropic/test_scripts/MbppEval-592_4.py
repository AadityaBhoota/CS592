import math

def binomial_Coeff(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n-k))

def sum_Of_product(n):
    total = 0
    for i in range(n):
        total += binomial_Coeff(n, i) * binomial_Coeff(n, i+1)
    return total

def check(candidate):
    assert sum_Of_product(3) == 15
    assert sum_Of_product(4) == 56
    assert sum_Of_product(1) == 1

check(binomial_Coeff)