import math

def is_polite(n):
    """
    Find the nth polite number.

    A polite number is a positive integer that can be expressed as the sum of two or more consecutive positive integers.

    Args:
        n (int): The index of the polite number to find.

    Returns:
        int: The nth polite number.
    """
    if n == 1:
        return 1
    
    count = 1
    num = 1
    
    while count < n:
        for i in range(1, num // 2 + 1):
            if (num - i * (i - 1) // 2) % i == 0:
                count += 1
                if count == n:
                    return num
        num += 1
    
    return num

def check(candidate):
    assert is_polite(7) == 11
    assert is_polite(4) == 7
    assert is_polite(9) == 13

check(is_polite)