import math

def area_tetrahedron(side):
    """
    Calculates the area of a tetrahedron.

    Parameters:
    side (float): The length of one side of the tetrahedron.

    Returns:
    float: The surface area of the tetrahedron.
    """
    # Calculate the area of one triangular face
    face_area = (math.sqrt(3) / 4) * (side ** 2)

    # Calculate the total surface area of the tetrahedron
    total_area = 4 * face_area

    return total_area

def check(candidate):
    assert area_tetrahedron(3)==15.588457268119894
    assert area_tetrahedron(20)==692.8203230275509
    assert area_tetrahedron(10)==173.20508075688772

check(area_tetrahedron)