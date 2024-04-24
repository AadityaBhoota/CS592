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

def is_multiply_prime(a):
    """
    Write a function that returns true if the given number is the multiplication of 3 prime numbers
    and false otherwise.
    Knowing that (a) is less than 100.
    """
    if a < 6:
        return False

    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            for j in range(2, int(i ** 0.5) + 1):
                if i % j == 0:
                    break
            else:
                for k in range(2, int((a / i) ** 0.5) + 1):
                    if (a // i) % k == 0:
                        break
                else:
                    if is_prime(i) and is_prime(a // i):
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