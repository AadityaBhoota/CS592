def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_multiply_prime(a):
    primes = [n for n in range(2, 100) if is_prime(n)]
    if a < 2:
        return False

    count = 0
    for prime in primes:
        if a % prime == 0:
            count += 1
            a //= prime
            if count == 3 and a == 1:
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