def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def newman_prime(n):
    def newman_shanks_williams(curr):
        if curr == 0:
            return 1
        return newman_shanks_williams(curr - 1) * newman_shanks_williams(curr - 1) + pow(-1, curr)
    
    if n <= 0:
        return None
    
    i = 0
    candidate = 0
    while i < n:
        candidate += 1
        if is_prime(candidate) and candidate == newman_shanks_williams(i):
            i += 1
    
    return candidate

# Test cases




def check(candidate):
    assert newman_prime(3) == 7
    assert newman_prime(4) == 17
    assert newman_prime(5) == 41

check(newman_prime)