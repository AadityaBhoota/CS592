def is_prime(n):
    """
    Helper function to check if a number is prime or not.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_multiply_prime(a):
    """
    Returns True if the given number is the multiplication of 3 prime numbers
    and False otherwise.
    Knowing that (a) is less than 100.
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    for i in range(2, int(a ** (1/3)) + 1):
        if a % i == 0:
            for j in range(i, int(a ** (1/2)) + 1):
                if a % j == 0:
                    if is_prime(i) and is_prime(j) and is_prime(a // (i * j)):
                        return True
    return False

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