from sympy import isprime

def is_multiply_prime(a):
    
    if a >= 100:
        return False
    
    factors = []
    
    for i in range(2, a):
        if isprime(i) and a % i == 0:
            factors.append(i)
    
    return len(factors) == 3

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