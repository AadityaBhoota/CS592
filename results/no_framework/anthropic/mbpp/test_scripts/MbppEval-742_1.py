import math

def area_tetrahedron(side):
    """
    Calculates the surface area of a tetrahedron.

    Args:
        side (float): The length of one side of the tetrahedron.

    Returns:
        float: The surface area of the tetrahedron.
    """
    area = (math.sqrt(3) * side ** 2)
    return area

# Examples




def check(candidate):
    assert area_tetrahedron(3)==15.588457268119894
    assert area_tetrahedron(20)==692.8203230275509
    assert area_tetrahedron(10)==173.20508075688772

check(area_tetrahedron)