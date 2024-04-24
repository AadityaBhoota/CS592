def find_Volume(l, b, h):
    volume = 0.5 * l * b * h
    return volume

# Test cases




def check(candidate):
    assert find_Volume(10,8,6) == 240
    assert find_Volume(3,2,2) == 6
    assert find_Volume(1,2,1) == 1

check(find_Volume)