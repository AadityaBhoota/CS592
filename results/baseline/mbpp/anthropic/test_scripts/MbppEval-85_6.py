import math

def surfacearea_sphere(r):
    '''
    Write a function to find the surface area of a sphere.

    Examples:
    surfacearea_sphere(10) == 1256.6370614359173
    surfacearea_sphere(15) == 2827.4333882308138
    surfacearea_sphere(20) == 5026.548245743669
    '''
    return 4 * math.pi * r ** 2

def check(candidate):
    assert math.isclose(surfacearea_sphere(10), 1256.6370614359173, rel_tol=0.001)
    assert math.isclose(surfacearea_sphere(15), 2827.4333882308138, rel_tol=0.001)
    assert math.isclose(surfacearea_sphere(20), 5026.548245743669, rel_tol=0.001)

check(surfacearea_sphere)