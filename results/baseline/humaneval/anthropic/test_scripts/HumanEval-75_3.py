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

    # Create a list of prime numbers up to 100
    primes = [2]
    for i in range(3, 100, 2):
        is_prime = True
        for j in primes:
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)

    # Check if a is the product of 3 prime numbers
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            for k in range(j + 1, len(primes)):
                if primes[i] * primes[j] * primes[k] == a:
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