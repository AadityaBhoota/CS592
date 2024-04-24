def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_multiply_prime(a):
    if a >= 100:
        return False
    
    primes = [x for x in range(2, 100) if is_prime(x)]
    
    for i in primes:
        for j in primes:
            for k in primes:
                if i * j * k == a:
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