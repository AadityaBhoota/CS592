def rectangle_area(l, b):
    """
    Write a function to find the area of a rectangle.

    Examples:
    rectangle_area(10, 20) == 200
    rectangle_area(10, 5) == 50
    rectangle_area(4, 2) == 8
    """
    area = l * b
    return area

def check(candidate):
    assert rectangle_area(10,20)==200
    assert rectangle_area(10,5)==50
    assert rectangle_area(4,2)==8

check(rectangle_area)