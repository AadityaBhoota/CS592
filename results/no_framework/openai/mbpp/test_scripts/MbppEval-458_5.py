def rectangle_area(l, b):
    '''
    Calculate the area of a rectangle given its length and breadth.

    Args:
    l (float): Length of the rectangle.
    b (float): Breadth of the rectangle.

    Returns:
    float: Area of the rectangle.
    '''
    return l * b

# Examples




def check(candidate):
    assert rectangle_area(10,20)==200
    assert rectangle_area(10,5)==50
    assert rectangle_area(4,2)==8

check(rectangle_area)