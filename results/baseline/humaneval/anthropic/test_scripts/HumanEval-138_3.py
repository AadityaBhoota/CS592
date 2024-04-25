def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers"""
    if n < 8:
        return False
    
    # Base case: n == 8
    if n == 8:
        return True
    
    # Recursive case: Check if n can be written as the sum of 4 even numbers
    for i in range(2, n-4, 2):
        for j in range(i+2, n-2, 2):
            for k in range(j+2, n, 2):
                if i + j + k + (n - i - j - k) == n:
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