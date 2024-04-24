import cmath

def polar_rect(r, theta):
    """
    Write a function to convert polar coordinates to rectangular coordinates.

    Examples:
    polar_rect(3, 4) == ((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j))
    polar_rect(4, 7) == ((8.06225774829855, 1.0516502125483738), (-2+2.4492935982947064e-16j))
    polar_rect(15, 17) == ((22.67156809750927, 0.8478169733934057), (-2+2.4492935982947064e-16j))
    """
    x = r * cmath.cos(cmath.radians(theta))
    y = r * cmath.sin(cmath.radians(theta))
    return ((round(abs(x), 10), round(cmath.phase(x), 10)), complex(round(y, 10), -2))

def check(candidate):
    assert polar_rect(3,4)==((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j))
    assert polar_rect(4,7)==((8.06225774829855, 1.0516502125483738), (-2+2.4492935982947064e-16j))
    assert polar_rect(15,17)==((22.67156809750927, 0.8478169733934057), (-2+2.4492935982947064e-16j))

check(polar_rect)