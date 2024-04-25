def parabola_directrix(a, b, c):
    """
    Write a function to find the directrix of a parabola.

    Examples:
    parabola_directrix(5, 3, 2) == -198
    parabola_directrix(9, 8, 4) == -2336
    parabola_directrix(2, 4, 6) == -130
    """
    return -b ** 2 / (4 * a)

def check(candidate):
    assert parabola_directrix(5,3,2)==-198
    assert parabola_directrix(9,8,4)==-2336
    assert parabola_directrix(2,4,6)==-130

check(parabola_directrix)