def is_equal_to_sum_even(n):
    if n % 2 != 0 or n < 8:  # If n is odd or less than 8, it's not possible
        return False
    return True

# Test cases




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