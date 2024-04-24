def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True

def is_polite(n):
    count = 1
    number = 1
    while count < n:
        number += 1
        if number % 2 == 0 and not is_prime(number):
            count += 1
    return number

# Test cases




def check(candidate):
    assert is_polite(7) == 11
    assert is_polite(4) == 7
    assert is_polite(9) == 13

check(is_polite)