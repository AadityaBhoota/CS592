def binomial_Coeff(n,k): 
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    def binomial_coefficient(n, k):
        return factorial(n) // (factorial(k) * factorial(n - k))

    sum_of_product = 0
    for i in range(1, n+1):
        sum_of_product += binomial_coefficient(n, i) * binomial_coefficient(n, i+1)

    return sum_of_product

# Test the function




def check(candidate):
    assert sum_Of_product(3) == 15
    assert sum_Of_product(4) == 56
    assert sum_Of_product(1) == 1

check(binomial_Coeff)