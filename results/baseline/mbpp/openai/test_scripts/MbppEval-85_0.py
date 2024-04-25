def surfacearea_sphere(r):
    # Calculate the surface area of a sphere using the formula 4 * pi * r^2
    surface_area = 4 * math.pi * r**2
    return surface_area

# Test the function




def check(candidate):
    assert math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001)
    assert math.isclose(surfacearea_sphere(15), 2827.4333882308138, rel_tol=0.001)
    assert math.isclose(surfacearea_sphere(20), 5026.548245743669, rel_tol=0.001)

check(surfacearea_sphere)