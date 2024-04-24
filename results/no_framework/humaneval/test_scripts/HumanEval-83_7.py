def starts_one_ends(n):
    count_start_with_1 = 9 * 10 ** (n - 1)  # Numbers that start with 1
    count_end_with_1 = 10 ** (n - 1)         # Numbers that end with 1

    total_count = count_start_with_1 + count_end_with_1
    return total_count

# Example Usage
n = 3
print(starts_one_ends(n))  # Output: 109

def check(candidate):

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(1) == 1
    assert candidate(2) == 18
    assert candidate(3) == 180
    assert candidate(4) == 1800
    assert candidate(5) == 18000

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"


check(starts_one_ends)