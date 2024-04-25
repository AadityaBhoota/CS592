import math

def prime_num(num):
    if num < 2:
        return False
    
    if num == 2:
        return True
    
    if num % 2 == 0:
        return False
    
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    
    return True

def check(candidate):
    assert prime_num(13)==True
    assert prime_num(7)==True
    assert prime_num(-1010)==False

check(prime_num)