def rectangle_area(l, b):
    '''
    Calculate the area of a rectangle given its length and breadth.

    Args:
    l (int): Length of the rectangle
    b (int): Breadth of the rectangle

    Returns:
    int: Area of the rectangle
    '''
    return l * b

# Test cases




def check(candidate):
    assert rectangle_area(10,20)==200
    assert rectangle_area(10,5)==50
    assert rectangle_area(4,2)==8

check(rectangle_area)