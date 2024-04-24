import math

def is_polite(n):
    """
    Write a function to find the nth polite number.

    The polite numbers are the numbers that can be expressed as the sum of two or more consecutive positive integers.
    The first few polite numbers are: 4, 6, 7, 10, 11, 12, 13, 14, 16, 18, 19, 20, 21, 22, 23, 24, 25, ...

    Args:
        n (int): The index of the polite number to find.

    Returns:
        int: The nth polite number.
    """
    count = 0
    num = 1
    while count < n:
        for i in range(1, num // 2 + 1):
            if (num * (num + 1)) // 2 - i * (i + 1) // 2 == num:
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