import cmath

def polar_rect(r, theta):
    """
    Converts polar coordinates to rectangular coordinates.

    Args:
        r (float): The magnitude (radius) of the polar coordinate.
        theta (float): The angle (in radians) of the polar coordinate.

    Returns:
        Tuple[float, complex]: A tuple containing the rectangular coordinates.
            The first element is the magnitude, and the second element is the
            complex number representation.
    """
    x = r * cmath.cos(theta)
    y = r * cmath.sin(theta)
    return (r, complex(x, y))

def check(candidate):
    assert polar_rect(3,4)==((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j))
    assert polar_rect(4,7)==((8.06225774829855, 1.0516502125483738), (-2+2.4492935982947064e-16j))
    assert polar_rect(15,17)==((22.67156809750927, 0.8478169733934057), (-2+2.4492935982947064e-16j))

check(polar_rect)