def unique_digits(x):
    def has_even_digit(n):
        return any(int(digit) % 2 == 0 for digit in str(n))

    return sorted([num for num in x if not has_even_digit(num)])

# Test cases



def check(candidate):

    # Check some simple cases
    assert candidate([15, 33, 1422, 1]) == [1, 15, 33]
    assert candidate([152, 323, 1422, 10]) == []
    assert candidate([12345, 2033, 111, 151]) == [111, 151]
    assert candidate([135, 103, 31]) == [31, 135]

    # Check some edge cases that are easy to work out by hand.
    assert True


check(unique_digits)