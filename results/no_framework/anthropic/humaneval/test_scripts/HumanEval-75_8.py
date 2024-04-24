def is_multiply_prime(a):
    """
    Returns True if the given number is the multiplication of 3 prime numbers, and False otherwise.
    Assuming that the input (a) is less than 100.
    """
    if a < 2:
        return False

    # Check if a is a product of three prime numbers
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            for j in range(i + 1, int(a / i) + 1):
                if a % j == 0:
                    for k in range(j + 1, int(a / (i * j)) + 1):
                        if a % k == 0 and is_prime(i) and is_prime(j) and is_prime(k):
                            return True
    return False

def is_prime(n):
    """
    Checks if a number is prime.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

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