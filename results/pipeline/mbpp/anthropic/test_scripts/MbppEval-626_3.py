def triangle_area(r):
    if r < 0:
        return -1
    elif r == 0:
        return 0
    else:
        return 0.5 * 2 * r * r

def check(candidate):
    assert triangle_area(-1) == None
    assert triangle_area(0) == 0
    assert triangle_area(2) == 4

check(triangle_area)