import math

def surfacearea_cylinder(r, h):
    # Calculate the lateral surface area of the cylinder
    lateral_area = 2 * math.pi * r * h

    # Calculate the top and bottom surface areas of the cylinder
    top_area = math.pi * (r ** 2)
    bottom_area = math.pi * (r ** 2)

    # Calculate the total surface area of the cylinder
    total_area = lateral_area + top_area + bottom_area

    return round(total_area, 2)

# Test the function with the given examples




def check(candidate):
    assert surfacearea_cylinder(10,5)==942.45
    assert surfacearea_cylinder(4,5)==226.18800000000002
    assert surfacearea_cylinder(4,10)==351.848

check(surfacearea_cylinder)