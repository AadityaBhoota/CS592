import math

def triangle_area(a, b, c):
    def is_valid_triangle(a, b, c):
        return a + b > c and a + c > b and b + c > a

    if not is_valid_triangle(a, b, c):
        return -1

    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    rounded_area = round(area, 2)
    
    return rounded_area

def check(candidate):

    # Check some simple cases
    assert candidate(3, 4, 5) == 6.00, "This prints if this assert fails 1 (good for debugging!)"
    assert candidate(1, 2, 10) == -1
    assert candidate(4, 8, 5) == 8.18
    assert candidate(2, 2, 2) == 1.73
    assert candidate(1, 2, 3) == -1
    assert candidate(10, 5, 7) == 16.25
    assert candidate(2, 6, 3) == -1

    # Check some edge cases that are easy to work out by hand.
    assert candidate(1, 1, 1) == 0.43, "This prints if this assert fails 2 (also good for debugging!)"
    assert candidate(2, 2, 10) == -1


check(triangle_area)