def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_multiply_prime(a):
    if a > 100:
        return False

    prime_count = 0
    for i in range(2, a):
        if is_prime(i) and a % i == 0:
            prime_count += 1
            if prime_count > 3:
                return False

    return prime_count == 3

# Test
print(is_multiply_prime(30))  # True

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