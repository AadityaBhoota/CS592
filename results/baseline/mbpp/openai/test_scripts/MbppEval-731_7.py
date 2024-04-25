def lateralsurface_cone(r, h):
    L = math.pi * r * math.sqrt(r**2 + h**2)
    return L

# Test the function with the provided examples




def check(candidate):
    assert lateralsurface_cone(5,12)==204.20352248333654
    assert lateralsurface_cone(10,15)==566.3586699569488
    assert lateralsurface_cone(19,17)==1521.8090132193388

check(lateralsurface_cone)