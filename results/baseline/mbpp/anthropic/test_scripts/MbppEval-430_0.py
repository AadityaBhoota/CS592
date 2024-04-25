def parabola_directrix(a, b, c):
    """
    Write a function to find the directrix of a parabola.

    Examples:
    parabola_directrix(5, 3, 2) == -198
    parabola_directrix(9, 8, 4) == -2336
    parabola_directrix(2, 4, 6) == -130
    """
    if a == 0:
        raise ValueError("'a' cannot be 0")
    
    # Using the formula: y = ax^2 + bx + c
    # The directrix is the line perpendicular to the axis of symmetry and passing through the focus
    # The focus is at (x, y) = (-b/(2a), -(b^2 - 4ac)/(4a))
    # The equation of the directrix is x = -b/(2a)
    
    directrix = -b / (2 * a)
    return directrix

def check(candidate):
    assert parabola_directrix(5,3,2)==-198
    assert parabola_directrix(9,8,4)==-2336
    assert parabola_directrix(2,4,6)==-130

check(parabola_directrix)