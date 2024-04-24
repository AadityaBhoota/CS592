def triangle_area(a, h):
    """Given length of a side and high return area for a triangle."""
    return 0.5 * a * h

# Test the function
print(triangle_area(5, 3))  # Output: 7.5



METADATA = {}


def check(candidate):
    assert candidate(5, 3) == 7.5
    assert candidate(2, 2) == 2.0
    assert candidate(10, 8) == 40.0


check(triangle_area)