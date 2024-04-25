def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_newman_shanks_williams_prime(n):
    if not is_prime(n):
        return False
    i = 0
    while True:
        if n == 2 ** i + 1:
            return True
        if 2 ** i + 1 > n:
            return False
        i += 1

def newman_prime(n):
    count = 0
    i = 2
    while True:
        if is_newman_shanks_williams_prime(i):
            count += 1
            if count == n:
                return i
        i += 1

def check(candidate):
    assert newman_prime(3) == 7
    assert newman_prime(4) == 17
    assert newman_prime(5) == 41

check(newman_prime)