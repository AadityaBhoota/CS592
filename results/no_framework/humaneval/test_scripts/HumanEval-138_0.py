def is_equal_to_sum_even(n):
    if n % 2 != 0 or n < 8:  # n should be even and a minimum of 8 for it to be written as the sum of 4 even numbers
        return False
    
    for i in range(2, n//2+1, 2):
        for j in range(2, n//2+1, 2):
            for k in range(2, n//2+1, 2):
                for l in range(2, n//2+1, 2):
                    if i + j + k + l == n:
                        return True
    return False

# Test cases
print(is_equal_to_sum_even(4))  # False
print(is_equal_to_sum_even(6))  # False
print(is_equal_to_sum_even(8))  # True

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