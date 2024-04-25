def triangle_area(a, h):
    """Given length of a side and height, return the area of a triangle."""
    
    # Calculate the area of the triangle
    area = (a * h) / 2
    
    return area



METADATA = {}


def check(candidate):
    assert candidate(5, 3) == 7.5
    assert candidate(2, 2) == 2.0
    assert candidate(10, 8) == 40.0


check(triangle_area)