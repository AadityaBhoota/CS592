def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers"""
    if n % 4 != 0:
        return False
    even_numbers = [2, 4, 6, 8]
    sum_of_even_numbers = sum(even_numbers)
    while sum_of_even_numbers < n:
        even_numbers = [num + 2 for num in even_numbers]
        sum_of_even_numbers = sum(even_numbers)
    return sum_of_even_numbers == n

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