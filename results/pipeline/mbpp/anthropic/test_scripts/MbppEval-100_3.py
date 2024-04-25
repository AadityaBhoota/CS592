def is_palindrome(n):
    """
    Check if a number is a palindrome.
    """
    original_n = n
    reversed_n = 0
    while n > 0:
        reversed_n = reversed_n * 10 + n % 10
        n //= 10
    return original_n == reversed_n

def next_smallest_palindrome(num):
    """
    Find the next smallest palindrome of a given integer.
    """
    if is_palindrome(num):
        return num
    
    num += 1
    while not is_palindrome(num):
        num += 1
    
    return num

def check(candidate):
    assert next_smallest_palindrome(99)==101
    assert next_smallest_palindrome(1221)==1331
    assert next_smallest_palindrome(120)==121

check(next_smallest_palindrome)