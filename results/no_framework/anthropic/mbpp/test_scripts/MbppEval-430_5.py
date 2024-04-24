def parabola_directrix(a, b, c):
    """
    Find the directrix of a parabola.

    The directrix of a parabola is a line that is perpendicular to the axis of
    symmetry and intersects the vertex. The equation of the directrix is
    given by:

    x = -b / (2a)

    Args:
        a (float): The coefficient of x^2 in the equation of the parabola.
        b (float): The coefficient of x in the equation of the parabola.
        c (float): The constant term in the equation of the parabola.

    Returns:
        float: The x-coordinate of the directrix.
    """
    return -b / (2 * a)

def check(candidate):
    assert parabola_directrix(5,3,2)==-198
    assert parabola_directrix(9,8,4)==-2336
    assert parabola_directrix(2,4,6)==-130

check(parabola_directrix)