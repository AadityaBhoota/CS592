def right_angle_triangle(a, b, c):
    if not is_valid_triangle(a, b, c):
        return False

    longest_side = max(a, b, c)
    sum_of_squares = a**2 + b**2 if longest_side == c else (a**2 + c**2 if longest_side == b else b**2 + c**2)

    return longest_side**2 == sum_of_squares

def check(candidate):

    # Check some simple cases
    assert candidate(3, 4, 5) == True, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(1, 2, 3) == False
    assert candidate(10, 6, 8) == True
    assert candidate(2, 2, 2) == False
    assert candidate(7, 24, 25) == True
    assert candidate(10, 5, 7) == False
    assert candidate(5, 12, 13) == True
    assert candidate(15, 8, 17) == True
    assert candidate(48, 55, 73) == True

    # Check some edge cases that are easy to work out by hand.
    assert candidate(1, 1, 1) == False, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate(2, 2, 10) == False


check(right_angle_triangle)