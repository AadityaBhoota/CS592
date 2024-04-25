def triangle_area(a, h):
    # Step 1: Calculate the area of the triangle
    area = 0.5 * a * h
    return area



METADATA = {}


def check(candidate):
    assert candidate(5, 3) == 7.5
    assert candidate(2, 2) == 2.0
    assert candidate(10, 8) == 40.0


check(triangle_area)