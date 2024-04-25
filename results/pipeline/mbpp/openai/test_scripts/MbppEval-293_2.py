import math

def otherside_rightangle(w, h):
    if w <= 0 or h <= 0:
        return "Invalid input. Sides of a triangle must be positive numbers."
    else:
        third_side = math.sqrt(w**2 + h**2)
        return third_side

def check(candidate):
    assert otherside_rightangle(7,8)==10.63014581273465
    assert otherside_rightangle(3,4)==5
    assert otherside_rightangle(7,15)==16.55294535724685

check(otherside_rightangle)