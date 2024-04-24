def largest_prime_factor(n: int):
    # Function to check if a number is prime
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    largest_prime = 0
    i = 2
    while i * i <= n:
        if n % i == 0:
            if is_prime(i):
                largest_prime = i
            if is_prime(n // i):
                largest_prime = n // i
        i += 1

    return largest_prime

# Test the function





METADATA = {}


def check(candidate):
    assert candidate(15) == 5
    assert candidate(27) == 3
    assert candidate(63) == 7
    assert candidate(330) == 11
    assert candidate(13195) == 29


check(largest_prime_factor)