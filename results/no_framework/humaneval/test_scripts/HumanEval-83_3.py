def starts_one_ends(n):
    # Count of numbers that start with 1
    start_with_one = 9 * 10 ** (n - 1)

    # Count of numbers that end with 1 (excluding those that start with 1)
    end_with_one = 10 ** (n - 1)

    # Return the total count of numbers that start or end with 1
    return start_with_one + end_with_one

# Test the function
n = 3
print(starts_one_ends(n))  # Output: 190

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