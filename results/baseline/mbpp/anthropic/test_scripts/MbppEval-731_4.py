import math

def lateralsurface_cone(r, h):
    """
    Write a function to find the lateral surface area of a cone given radius r and the height h.

    Examples:
    lateralsurface_cone(5, 12) == 204.20352248333654
    lateralsurface_cone(10, 15) == 566.3586699569488
    lateralsurface_cone(19, 17) == 1521.8090132193388
    """
    # Calculate the slant height of the cone
    slant_height = math.sqrt(r**2 + h**2)
    
    # Calculate the lateral surface area of the cone
    lateral_surface_area = math.pi * r * slant_height
    
    return lateral_surface_area

def check(candidate):
    assert lateralsurface_cone(5,12)==204.20352248333654
    assert lateralsurface_cone(10,15)==566.3586699569488
    assert lateralsurface_cone(19,17)==1521.8090132193388

check(lateralsurface_cone)