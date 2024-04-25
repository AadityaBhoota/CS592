def is_prime(number):
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

def largest_prime_factor(n: int):
    factor = 2

    while factor < n:
        if n % factor == 0:
            if is_prime(factor):
                n //= factor
            else:
                factor += 1
        else:
            factor += 1

    return n



METADATA = {}


def check(candidate):
    assert candidate(15) == 5
    assert candidate(27) == 3
    assert candidate(63) == 7
    assert candidate(330) == 11
    assert candidate(13195) == 29


check(largest_prime_factor)