def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def binomial_Coeff(n, k):
    return factorial(n) // (factorial(k) * factorial(n-k))

def sum_Of_product(n):
    total = 0
    for k in range(n):
        total += binomial_Coeff(n, k) * binomial_Coeff(n, k+1)
    return total

def check(candidate):
    assert sum_Of_product(3) == 15
    assert sum_Of_product(4) == 56
    assert sum_Of_product(1) == 1

check(binomial_Coeff)