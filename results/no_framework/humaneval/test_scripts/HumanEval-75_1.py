def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_multiply_prime(a):
    if a < 6:
        return False
    
    for i in range(2, a):
        if a % i == 0 and is_prime(i):
            # If we find a factor that is prime, reduce a by that factor
            a //= i
            if a % i == 0:
                return False
    if a > 1 and is_prime(a):
        return True
    return False

# Test the function
assert is_multiply_prime(30) == True
assert is_multiply_prime(35) == False

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