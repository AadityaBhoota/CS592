def rectangle_area(l, b):
    '''
    This function calculates the area of a rectangle given its length (l) and breadth (b).
    
    Parameters:
    l (int): Length of the rectangle
    b (int): Breadth of the rectangle
    
    Returns:
    int: Area of the rectangle
    '''
    return l * b

# Test cases
assert rectangle_area(10, 20) == 200
assert rectangle_area(10, 5) == 50
assert rectangle_area(4, 2) == 8

def check(candidate):
    assert rectangle_area(10,20)==200
    assert rectangle_area(10,5)==50
    assert rectangle_area(4,2)==8

check(rectangle_area)