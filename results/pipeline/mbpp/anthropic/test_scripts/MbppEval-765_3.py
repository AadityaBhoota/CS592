import math

def is_polite(n):
    """
    Find the nth polite number.
    """
    if n == 1:
        return 1

    left, right = 2, n * 2
    while left <= right:
        mid = (left + right) // 2
        divisors = 0
        for i in range(1, int(math.sqrt(mid)) + 1):
            if mid % i == 0:
                divisors += 1
                if i != mid // i:
                    divisors += 1
        if divisors == n:
            return mid
        elif divisors < n:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def check(candidate):
    assert is_polite(7) == 11
    assert is_polite(4) == 7
    assert is_polite(9) == 13

check(is_polite)