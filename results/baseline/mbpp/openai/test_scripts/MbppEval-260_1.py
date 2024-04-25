def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def newman_prime(n):
    result = 0
    count = 0
    while count < n:
        result += 1
        if is_prime(result) and is_prime(2**result + 1):
            count += 1
    return result

# Test cases




def check(candidate):
    assert newman_prime(3) == 7
    assert newman_prime(4) == 17
    assert newman_prime(5) == 41

check(newman_prime)