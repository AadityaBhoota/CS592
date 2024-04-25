def prime_num(num):
    """
    Check if the given integer is a prime number.

    Args:
        num (int): The number to be checked.

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