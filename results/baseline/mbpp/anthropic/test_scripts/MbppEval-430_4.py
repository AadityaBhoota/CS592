def parabola_directrix(a, b, c):
    """
    Write a function to find the directrix of a parabola.

    Examples:
    parabola_directrix(5, 3, 2) == -198
    parabola_directrix(9, 8, 4) == -2336
    parabola_directrix(2, 4, 6) == -130
    """
    # Calculate the vertex of the parabola
    x_vertex = -b / (2 * a)
    y_vertex = a * (x_vertex ** 2) + b * x_vertex + c
    
    # Calculate the directrix
    directrix = y_vertex - (1 / (4 * a))
    return directrix

def check(candidate):
    assert parabola_directrix(5,3,2)==-198
    assert parabola_directrix(9,8,4)==-2336
    assert parabola_directrix(2,4,6)==-130

check(parabola_directrix)