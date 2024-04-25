import math

def surfacearea_cylinder(r, h):
    # Step 1: Calculate the surface area of the two circular ends of the cylinder
    circular_end_area = 2 * math.pi * (r ** 2)
    
    # Step 2: Calculate the lateral surface area of the cylinder
    lateral_area = 2 * math.pi * r * h
    
    # Step 3: Add the two calculated surface areas to get the total surface area of the cylinder
    total_surface_area = circular_end_area + lateral_area
    
    return total_surface_area

def check(candidate):
    assert surfacearea_cylinder(10,5)==942.45
    assert surfacearea_cylinder(4,5)==226.18800000000002
    assert surfacearea_cylinder(4,10)==351.848

check(surfacearea_cylinder)