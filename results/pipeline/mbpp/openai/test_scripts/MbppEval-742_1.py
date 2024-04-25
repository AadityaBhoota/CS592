import math

def area_tetrahedron(side):
    height = (math.sqrt(6) / 3) * side
    area = math.sqrt(3) * side**2 / 4
    return area

def check(candidate):
    assert area_tetrahedron(3)==15.588457268119894
    assert area_tetrahedron(20)==692.8203230275509
    assert area_tetrahedron(10)==173.20508075688772

check(area_tetrahedron)