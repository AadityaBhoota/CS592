import math

def is_prm(p, n):
    # Function to check if number is prime
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def is_polite(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        if is_prm(n, num):
             count += 1
    return num

def check(candidate):
    assert is_polite(7) == 11
    assert is_polite(4) == 7
    assert is_polite(9) == 13

check(is_polite)