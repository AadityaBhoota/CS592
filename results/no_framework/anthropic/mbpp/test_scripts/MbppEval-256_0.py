def count_Primes_nums(n):
    """
    Write a python function that takes in a non-negative number and returns the number of prime numbers less than the given non-negative number.

    Examples:
    count_Primes_nums(5) == 2
    count_Primes_nums(10) == 4
    count_Primes_nums(100) == 25
    """
    if n <= 2:
        return 0

    is_prime = [True] * n
    is_prime[0] = is_prime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, n, i):
                is_prime[j] = False

    return sum(is_prime)

def check(candidate):
    assert count_Primes_nums(5) == 2
    assert count_Primes_nums(10) == 4
    assert count_Primes_nums(100) == 25

check(count_Primes_nums)