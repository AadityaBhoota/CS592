def triangle_area(r):
    base = 2 * r
    height = r
    area = (base * height) / 2
    return area

def check(candidate):
    assert triangle_area(-1) == None
    assert triangle_area(0) == 0
    assert triangle_area(2) == 4

check(triangle_area)