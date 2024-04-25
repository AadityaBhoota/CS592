def lateralsurface_cube(l):
    if l <= 0:
        raise ValueError("Side length of the cube must be a positive number")
    
    lateral_surface_area = 4 * l * l
    return lateral_surface_area

def check(candidate):
    assert lateralsurface_cube(5)==100
    assert lateralsurface_cube(9)==324
    assert lateralsurface_cube(10)==400

check(lateralsurface_cube)