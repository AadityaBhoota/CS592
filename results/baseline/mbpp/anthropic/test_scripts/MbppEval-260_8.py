def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def newman_prime(n):
    """
    Find the nth Newman-Shanks-Williams prime number.

    Examples:
    newman_prime(3) == 7
    newman_prime(4) == 17
    newman_prime(5) == 41
    """
    count = 0
    num = 2
    while count < n:
        if is_prime(num) and is_prime(num + 2) and is_prime(num + 6):
            count += 1
        num += 1
    return num - 1

def check(candidate):
    assert newman_prime(3) == 7
    assert newman_prime(4) == 17
    assert newman_prime(5) == 41

check(newman_prime)