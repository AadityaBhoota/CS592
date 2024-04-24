def is_equal_to_sum_even(n):
    if n % 2 != 0:  # Check if n is not even
        return False

    count = 0
    for i in range(2, n // 2 + 1, 2):  # Check even numbers from 2 to n//2
        if n - i * 4 == 0:  # Check if n can be written as the sum of 4 even numbers
            count += 1

    return count == 1  # Return True if only one combination exists, False otherwise

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