def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def newman_prime(n): 
    def ns_prime(candidate):
        return is_prime((2**candidate) * candidate - 1)
    
    count = 0
    num = 0
    
    while count < n:
        if ns_prime(num):
            count += 1
            if count == n:
                return num
        num += 1

def check(candidate):
    assert newman_prime(3) == 7
    assert newman_prime(4) == 17
    assert newman_prime(5) == 41

check(newman_prime)