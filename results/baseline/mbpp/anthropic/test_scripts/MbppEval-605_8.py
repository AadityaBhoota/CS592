def prime_num(num):
    '''
    Write a function to check if the given integer is a prime number.

    Examples:
    prime_num(13) == True
    prime_num(7) == True
    prime_num(-1010) == False
    '''
def is_prime(num):
    """
    Checks if a given integer is a prime number.

    Args:
        num (int): The integer to be checked.

    Returns:
        bool: True if the number is prime, False otherwise.
    """
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def check(candidate):
    assert prime_num(13)==True
    assert prime_num(7)==True
    assert prime_num(-1010)==False

check(prime_num)