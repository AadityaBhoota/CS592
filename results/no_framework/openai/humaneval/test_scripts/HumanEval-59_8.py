def largest_prime_factor(n: int):
    # Function to check if a number is prime
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    # Function to find all prime factors of a number
    def prime_factors(num):
        factors = []
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            else:
                num //= i
                factors.append(i)
        if num > 1:
            factors.append(num)
        return factors

    # Find all prime factors of n and return the largest one
    factors = prime_factors(n)
    largest_prime = max(factor for factor in factors if is_prime(factor))
    return largest_prime

# Test the function with the provided test cases





METADATA = {}


def check(candidate):
    assert candidate(15) == 5
    assert candidate(27) == 3
    assert candidate(63) == 7
    assert candidate(330) == 11
    assert candidate(13195) == 29


check(largest_prime_factor)