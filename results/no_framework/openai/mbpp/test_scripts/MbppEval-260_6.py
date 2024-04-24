def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def newman_prime(n):
    nsw_primes = [2]
    num = 3
    while len(nsw_primes) < n:
        if all(num % prime != 0 for prime in nsw_primes):
            nsw_primes.append(num)
        num += 2
    return nsw_primes[n - 1]

# Test cases




def check(candidate):
    assert newman_prime(3) == 7
    assert newman_prime(4) == 17
    assert newman_prime(5) == 41

check(newman_prime)