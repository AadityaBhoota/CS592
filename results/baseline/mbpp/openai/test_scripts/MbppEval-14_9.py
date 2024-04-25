def find_Volume(l, b, h):
    # The formula for the volume of a triangular prism is V = (1/2) * base * height * length
    volume = 0.5 * b * h * l
    return volume

# Test cases




def check(candidate):
    assert find_Volume(10,8,6) == 240
    assert find_Volume(3,2,2) == 6
    assert find_Volume(1,2,1) == 1

check(find_Volume)