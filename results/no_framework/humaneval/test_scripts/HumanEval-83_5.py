def starts_one_ends(n):
    if n == 1:
        return 1
    else:
        count = 2  # For numbers that start or end with 1
        count += 8 * 9 ** (n - 2)  # For numbers that start with 1
        count += 8 * 9 ** (n - 2)  # For numbers that end with 1
        return count

# Test the function
print(starts_one_ends(1))  # Output: 1
print(starts_one_ends(2))  # Output: 18
print(starts_one_ends(3))  # Output: 162

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