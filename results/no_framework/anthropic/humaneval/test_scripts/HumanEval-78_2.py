def is_prime(n):
    """
    Helper function to check if a number is prime.
    """
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def hex_key(num):
    """
    Function that counts the number of prime hexadecimal digits in a given hexadecimal number.
    """
    primes = [2, 3, 5, 7, 11, 13]
    prime_count = 0

    for char in num:
        if char.isdigit():
            if int(char) in primes:
                prime_count += 1
        else:
            if char in "BD":
                prime_count += 1

    return prime_count

def check(candidate):

    # Check some simple cases
    assert candidate("AB") == 1, "First test error: " + str(candidate("AB"))      
    assert candidate("1077E") == 2, "Second test error: " + str(candidate("1077E"))  
    assert candidate("ABED1A33") == 4, "Third test error: " + str(candidate("ABED1A33"))      
    assert candidate("2020") == 2, "Fourth test error: " + str(candidate("2020"))  
    assert candidate("123456789ABCDEF0") == 6, "Fifth test error: " + str(candidate("123456789ABCDEF0"))      
    assert candidate("112233445566778899AABBCCDDEEFF00") == 12, "Sixth test error: " + str(candidate("112233445566778899AABBCCDDEEFF00"))  


    # Check some edge cases that are easy to work out by hand.
    assert candidate([]) == 0


check(hex_key)