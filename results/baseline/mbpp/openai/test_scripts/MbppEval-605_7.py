def prime_num(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

# Test cases




def check(candidate):
    assert prime_num(13)==True
    assert prime_num(7)==True
    assert prime_num(-1010)==False

check(prime_num)