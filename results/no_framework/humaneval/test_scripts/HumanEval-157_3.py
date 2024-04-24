def right_angle_triangle(a, b, c):
    # Sort the sides in ascending order
    sides = sorted([a, b, c])
    
    # Check if it forms a right-angled triangle using Pythagorean theorem
    return sides[0]**2 + sides[1]**2 == sides[2]**2


# Test cases
print(right_angle_triangle(3, 4, 5))  # Output: True
print(right_angle_triangle(1, 2, 3))  # Output: False

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