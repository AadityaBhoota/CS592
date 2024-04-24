def is_equal_to_sum_even(n):
    count = 0
    for i in range(2, n // 2 + 1, 2):
        if n - i >= 0:
            count += 1
    return count == 4

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