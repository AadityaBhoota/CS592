def parabola_directrix(a, b, c):
    """
    Find the directrix of a parabola.

    Args:
        a (float): The coefficient of the squared term in the equation of the parabola.
        b (float): The coefficient of the linear term in the equation of the parabola.
        c (float): The constant term in the equation of the parabola.

    Returns:
        float: The y-coordinate of the directrix of the parabola.
    """
    return -b / (2 * a)

def check(candidate):
    assert parabola_directrix(5,3,2)==-198
    assert parabola_directrix(9,8,4)==-2336
    assert parabola_directrix(2,4,6)==-130

check(parabola_directrix)