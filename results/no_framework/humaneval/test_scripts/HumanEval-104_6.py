def unique_digits(x):
    def has_no_even_digit(num):
        return all(int(digit) % 2 != 0 for digit in str(num))
    
    return sorted([num for num in x if has_no_even_digit(num)])

# Test the function
print(unique_digits([15, 33, 1422, 1]))  # [1, 15, 33]
print(unique_digits([152, 323, 1422, 10]))  # []

def check(candidate):

    # Check some simple cases
    assert candidate([15, 33, 1422, 1]) == [1, 15, 33]
    assert candidate([152, 323, 1422, 10]) == []
    assert candidate([12345, 2033, 111, 151]) == [111, 151]
    assert candidate([135, 103, 31]) == [31, 135]

    # Check some edge cases that are easy to work out by hand.
    assert True


check(unique_digits)