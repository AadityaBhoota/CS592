import math

def area_tetrahedron(side):
    '''
    Calculates the area of a tetrahedron.

    Args:
        side (float): The length of one side of the tetrahedron.

    Returns:
        float: The total surface area of the tetrahedron.
    '''
    # Calculate the area of one triangular face
    face_area = (math.sqrt(3) / 4) * (side ** 2)

    # Calculate the total surface area by multiplying the face area by 4
    total_area = 4 * face_area

    return round(total_area, 10)

def check(candidate):
    assert area_tetrahedron(3)==15.588457268119894
    assert area_tetrahedron(20)==692.8203230275509
    assert area_tetrahedron(10)==173.20508075688772

check(area_tetrahedron)