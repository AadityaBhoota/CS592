def newman_prime(n): 
    coefficients = expand_expression(n)
    return coefficients[2**n]

def expand_expression(n):
    coefficients = [1]  # Initial coefficient
    for _ in range(2**n):
        new_coefficients = [0] * (len(coefficients) + 2)
        for i in range(len(coefficients)):
            new_coefficients[i] += coefficients[i]  # Coefficient for x^0
            new_coefficients[i+1] += coefficients[i]  # Coefficient for x^1
            new_coefficients[i+2] += coefficients[i]  # Coefficient for x^2
        coefficients = new_coefficients
    return coefficients

def check(candidate):
    assert newman_prime(3) == 7
    assert newman_prime(4) == 17
    assert newman_prime(5) == 41

check(newman_prime)