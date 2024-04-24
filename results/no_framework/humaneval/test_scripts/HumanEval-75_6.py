def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_multiply_prime(a):
    if a < 2:
        return False
    
    prime_factors = []
    for i in range(2, a):
        if is_prime(i) and a % i == 0:
            prime_factors.append(i)
    
    if len(prime_factors) == 3:
        product = 1
        for factor in prime_factors:
            product *= factor
        if product == a:
            return True
    
    return False

# Test the function


def check(candidate):

    assert candidate(5) == False
    assert candidate(30) == True
    assert candidate(8) == True
    assert candidate(10) == False
    assert candidate(125) == True
    assert candidate(3 * 5 * 7) == True
    assert candidate(3 * 6 * 7) == False
    assert candidate(9 * 9 * 9) == False
    assert candidate(11 * 9 * 9) == False
    assert candidate(11 * 13 * 7) == True


check(is_multiply_prime)