def starts_one_ends(n):
    if n <= 0:
        return 0

    # Count of numbers that start with 1
    start_with_one = 9 * 10 ** (n - 1)

    # Count of numbers that end with 1
    end_with_one = 10 ** (n - 1)

    return start_with_one + end_with_one - 1  # Subtract one to eliminate duplicates

# Test the function
n = 3
result = starts_one_ends(n)
print(result)

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