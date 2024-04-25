import math

def triangle_area(r):
    diameter = 2 * r
    base = diameter
    height = r
    return 0.5 * base * height

def check(candidate):
    assert triangle_area(-1) == None
    assert triangle_area(0) == 0
    assert triangle_area(2) == 4

check(triangle_area)