def triangle_area(a, h):
    """
    Given the length of a side and height, return the area of a triangle.
    
    Parameters:
    a (float): Length of a side of the triangle
    h (float): Height of the triangle
    
    Returns:
    float: Area of the triangle
    """
    area = 0.5 * a * h
    return area

# Test the function with the example values




METADATA = {}


def check(candidate):
    assert candidate(5, 3) == 7.5
    assert candidate(2, 2) == 2.0
    assert candidate(10, 8) == 40.0


check(triangle_area)