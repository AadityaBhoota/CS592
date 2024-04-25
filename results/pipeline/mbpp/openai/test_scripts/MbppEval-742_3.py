import math

def area_tetrahedron(side):
    # Step 1: Calculate the height of the tetrahedron
    height = (side * math.sqrt(6)) / 3

    # Step 2: Calculate the area of an equilateral triangle
    area_triangle = (math.sqrt(3) * side**2) / 4

    # Step 3: Calculate the total surface area of the tetrahedron
    total_area = 4 * area_triangle

    return total_area

def check(candidate):
    assert area_tetrahedron(3)==15.588457268119894
    assert area_tetrahedron(20)==692.8203230275509
    assert area_tetrahedron(10)==173.20508075688772

check(area_tetrahedron)