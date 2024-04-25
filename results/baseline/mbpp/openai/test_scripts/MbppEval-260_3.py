def newman_prime(n):
    if n <= 0:
        return None

    i = 1
    count = 0
    while count < n:
        num = 2 ** i - 1
        if is_prime(num):
            count += 1
        i += 1

    return num

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False

    for i in range(3, int(num ** 0.5) + 1, 2):
        if num % i == 0:
            return False

    return True

# Test cases




def check(candidate):
    assert newman_prime(3) == 7
    assert newman_prime(4) == 17
    assert newman_prime(5) == 41

check(newman_prime)