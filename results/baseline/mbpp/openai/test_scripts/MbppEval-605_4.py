def prime_num(num):
    '''
    Write a function to check if the given integer is a prime number.

    Examples:
    prime_num(13) == True
    prime_num(7) == True
    prime_num(-1010) == False
    '''
def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

# Test the function




def check(candidate):
    assert prime_num(13)==True
    assert prime_num(7)==True
    assert prime_num(-1010)==False

check(prime_num)