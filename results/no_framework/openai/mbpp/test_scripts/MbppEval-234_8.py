def volume_cube(l):
    return l**3

# Test the function with examples




def check(candidate):
    assert volume_cube(3)==27
    assert volume_cube(2)==8
    assert volume_cube(5)==125

check(volume_cube)