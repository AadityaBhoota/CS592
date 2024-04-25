from math import tan, pi

def area_polygon(s, l):
    if s <= 0 or l < 3:
        raise ValueError("Invalid input values. Side length should be positive and number of sides should be at least 3.")
    
    a = s / (2 * tan(pi / l))
    area = (l * s * a) / 2
    
    return area

def check(candidate):
    assert math.isclose(area_polygon(4, 20), 400., rel_tol=0.001)
    assert math.isclose(area_polygon(10, 15), 1731.197, rel_tol=0.001)
    assert math.isclose(area_polygon(9, 7), 302.909, rel_tol=0.001)

check(area_polygon)