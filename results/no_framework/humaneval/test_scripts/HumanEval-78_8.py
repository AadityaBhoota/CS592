def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def hex_key(num):
    primes = {'2', '3', '5', '7', 'B', 'D'}
    count = 0
    for digit in num:
        if digit in primes:
            count += 1

    return count

# Test cases
print(hex_key("AB"))         # Output: 1
print(hex_key("1077E"))      # Output: 2
print(hex_key("ABED1A33"))   # Output: 4
print(hex_key("123456789ABCDEF0"))  # Output: 6
print(hex_key("2020"))       # Output: 2

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