import math
def lateralsurface_cone(r, h):
    # Formula to calculate the lateral surface area of a cone: π*r*l, where l is the slant height
    l = math.sqrt(r**2 + h**2)  # Slant height of the cone
    lateral_surface_area = math.pi * r * l
    return lateral_surface_area

# Test cases




def check(candidate):
    assert lateralsurface_cone(5,12)==204.20352248333654
    assert lateralsurface_cone(10,15)==566.3586699569488
    assert lateralsurface_cone(19,17)==1521.8090132193388

check(lateralsurface_cone)