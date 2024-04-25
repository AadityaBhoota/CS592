def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def newman_prime(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        newman_num = 2**num - 1
        if is_prime(newman_num):
            count += 1
    return newman_num

# Test cases




def check(candidate):
    assert newman_prime(3) == 7
    assert newman_prime(4) == 17
    assert newman_prime(5) == 41

check(newman_prime)