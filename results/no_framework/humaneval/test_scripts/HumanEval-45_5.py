def triangle_area(a, h):
    """
    Given length of a base and height, return the area of a triangle.
    
    Arguments:
    a -- length of the base
    h -- height of the triangle
    
    Returns:
    Area of the triangle
    """
    area = 0.5 * a * h
    return area

# Test the function
print(triangle_area(5, 3))  # Output: 7.5



METADATA = {}


def check(candidate):
    assert candidate(5, 3) == 7.5
    assert candidate(2, 2) == 2.0
    assert candidate(10, 8) == 40.0


check(triangle_area)