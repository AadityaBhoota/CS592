import math

def factorize(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n = n // 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i

    if n > 2:
        factors.append(n)
    
    return factors

def count_distinct_prime_factors(n):
    prime_factors = factorize(n)
    prime_factors_set = set(prime_factors)
    return len(prime_factors_set)

def count_total_divisors(prime_factors):
    total_divisors = 1
    for factor in set(prime_factors):
        total_divisors *= prime_factors.count(factor) + 1
    return total_divisors

def is_polite(n):
    while True:
        prime_factors = factorize(n)
        total_divisors = count_total_divisors(prime_factors)
        
        if total_divisors >= n + 2:
            break
        
        n += 1
    
    return n

def check(candidate):
    assert is_polite(7) == 11
    assert is_polite(4) == 7
    assert is_polite(9) == 13

check(is_polite)