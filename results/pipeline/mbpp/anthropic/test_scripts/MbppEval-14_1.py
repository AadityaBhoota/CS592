def find_Volume(l, b, h):
    volume = (1/2) * b * h * l
    return volume

def check(candidate):
    assert find_Volume(10,8,6) == 240
    assert find_Volume(3,2,2) == 6
    assert find_Volume(1,2,1) == 1

check(find_Volume)