def right_angle_triangle(a, b, c):
    # Determine the longest side (hypotenuse)
    hypotenuse = max(a, b, c)
    
    # Calculate the squares of the other two sides
    a_squared = a ** 2
    b_squared = b ** 2
    c_squared = c ** 2
    
    # Check if the square of the hypotenuse is equal to the sum of the squares of the other two sides
    if hypotenuse ** 2 == a_squared + b_squared or hypotenuse ** 2 == a_squared + c_squared or hypotenuse ** 2 == b_squared + c_squared:
        return True
    else:
        return False

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