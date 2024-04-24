def triangle_area(a, h):
    """Given length of a side and height, return area of a triangle."""
    area = 0.5 * a * h
    return area

# Test the function with the provided example




METADATA = {}


def check(candidate):
    assert candidate(5, 3) == 7.5
    assert candidate(2, 2) == 2.0
    assert candidate(10, 8) == 40.0


check(triangle_area)