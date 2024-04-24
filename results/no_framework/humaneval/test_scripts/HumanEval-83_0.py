def starts_one_ends(n):
    count = 0

    for i in range(10**(n-1), 10**n):
        num_str = str(i)
        if num_str[0] == '1' or num_str[-1] == '1':
            count += 1

    return count

# Test the function with n = 2
print(starts_one_ends(2))  # Output should be 19

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