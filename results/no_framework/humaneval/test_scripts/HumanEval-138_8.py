def is_equal_to_sum_even(n):
    if n % 2 != 0 or n < 8:
        return False
    
    for a in range(2, n//2 + 1, 2):
        for b in range(2, n//2 + 1, 2):
            for c in range(2, n//2 + 1, 2):
                d = n - a - b - c
                if d % 2 == 0 and d >= 2:
                    return True
    
    return False

# Test cases
print(is_equal_to_sum_even(4))  # Output: False
print(is_equal_to_sum_even(6))  # Output: False
print(is_equal_to_sum_even(8))  # Output: True

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