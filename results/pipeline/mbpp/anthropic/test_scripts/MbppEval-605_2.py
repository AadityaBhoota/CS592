def prime_num(num):
    """
    Write a function to check if the given integer is a prime number.

    Examples:
    prime_num(13) == True
    prime_num(7) == True
    prime_num(-1010) == False
    """
    is_prime = True

    # Handle negative numbers
    if num < 0:
        is_prime = False
        return is_prime

    # Handle 0 and 1
    if num in [0, 1]:
        is_prime = False
        return is_prime

    # Check if the number is divisible by any number from 2 to the square root of the number
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

    return is_prime

def check(candidate):
    assert prime_num(13)==True
    assert prime_num(7)==True
    assert prime_num(-1010)==False

check(prime_num)