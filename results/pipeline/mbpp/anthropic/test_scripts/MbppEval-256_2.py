def count_Primes_nums(n):
    """
    Write a python function that takes in a non-negative number and returns the number of prime numbers less than the given non-negative number.

    Examples:
    count_Primes_nums(5) == 2
    count_Primes_nums(10) == 4
    count_Primes_nums(100) == 25
    """
    if n < 2:
        return 0
    
    count = 0
    for i in range(2, n):
        if is_prime(i):
            count += 1
    return count

def is_prime(x):
    """
    Helper function to check if a number is prime.
    """
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

def check(candidate):
    assert count_Primes_nums(5) == 2
    assert count_Primes_nums(10) == 4
    assert count_Primes_nums(100) == 25

check(count_Primes_nums)