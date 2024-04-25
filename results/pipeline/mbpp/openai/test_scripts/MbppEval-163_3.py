from math import tan, pi

def area_polygon(s, n):
    a = s / (2 * tan(pi / n))
    area = 0.5 * n * s * a
    return area

def check(candidate):
    assert math.isclose(area_polygon(4, 20), 400., rel_tol=0.001)
    assert math.isclose(area_polygon(10, 15), 1731.197, rel_tol=0.001)
    assert math.isclose(area_polygon(9, 7), 302.909, rel_tol=0.001)

check(area_polygon)