def unique_digits(x):
    unique_list = []
    for num in x:
        has_even_digit = False
        for digit in str(num):
            if int(digit) % 2 == 0:
                has_even_digit = True
                break
        if not has_even_digit:
            unique_list.append(num)
    unique_list.sort()
    return unique_list

def check(candidate):

    # Check some simple cases
    assert candidate([15, 33, 1422, 1]) == [1, 15, 33]
    assert candidate([152, 323, 1422, 10]) == []
    assert candidate([12345, 2033, 111, 151]) == [111, 151]
    assert candidate([135, 103, 31]) == [31, 135]

    # Check some edge cases that are easy to work out by hand.
    assert True


check(unique_digits)