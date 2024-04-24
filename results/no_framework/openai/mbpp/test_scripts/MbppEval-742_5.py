import math

def area_tetrahedron(side):
    # Calculate the height of the tetrahedron
    height = math.sqrt(2/3) * side

    # Calculate the area of the tetrahedron using the formula: sqrt(3) * side^2
    area = math.sqrt(3) * side**2

    return area

# Test the function




def check(candidate):
    assert area_tetrahedron(3)==15.588457268119894
    assert area_tetrahedron(20)==692.8203230275509
    assert area_tetrahedron(10)==173.20508075688772

check(area_tetrahedron)