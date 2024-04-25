def newman_prime(n):
    primes = []
    num = 2
    while len(primes) < n:
        if is_prime(num) and is_increasing_digits(num):
            primes.append(num)
        num += 1
    return primes[-1]

def is_increasing_digits(n):
    digits = [int(d) for d in str(n)]
    for i in range(1, len(digits)):
        if digits[i] <= digits[i-1]:
            return False
    return True

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def check(candidate):
    assert newman_prime(3) == 7
    assert newman_prime(4) == 17
    assert newman_prime(5) == 41

check(newman_prime)