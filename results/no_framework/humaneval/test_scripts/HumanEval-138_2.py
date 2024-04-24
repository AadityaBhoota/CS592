def is_equal_to_sum_even(n):
    count_even = 0
    for i in range(2, n):
        if i % 2 == 0 and n - i >= 0:
            count_even += 1
            if count_even == 4 and n - i == 0:
                return True
    return False

# Testing the function
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