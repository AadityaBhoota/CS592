def rectangle_area(l, b):
    return l * b

# Test cases




def check(candidate):
    assert rectangle_area(10,20)==200
    assert rectangle_area(10,5)==50
    assert rectangle_area(4,2)==8

check(rectangle_area)