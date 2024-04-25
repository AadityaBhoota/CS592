def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers"""
    if n < 8 or n % 2 != 0:
        return False

    for a in range(2, n//2, 2):
        for b in range(a, n//2, 2):
            for c in range(b, n//2, 2):
                d = n - a - b - c
                if d > 0 and d % 2 == 0:
                    return True

    return False

def check(candidate):
    assert candidate(4) == False
    assert candidate(6) == False
    assert candidate(8) == True
    assert candidate(10) == True
    assert candidate(11) == False
    assert candidate(12) == True
    assert candidate(13) == False
    assert candidate(16) == True

check(is_equal_to_sum_even)