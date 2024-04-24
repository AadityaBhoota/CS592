def is_multiply_prime(a):
    """
    Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less then 100.
    Example:
    is_multiply_prime(30) == True
    30 = 2 * 3 * 5
    """
    if a < 2:
        return False

    prime_factors = []
    for i in range(2, int(a ** 0.5) + 1):
        while a % i == 0:
            prime_factors.append(i)
            a //= i

    if a > 1:
        prime_factors.append(a)

    if len(prime_factors) != 3:
        return False

    for factor in prime_factors:
        if not is_prime(factor):
            return False

    return True

def is_prime(n):
    """
    Helper function to check if a number is prime.
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