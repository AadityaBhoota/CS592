def surfacearea_cube(l):
    return 6 * l ** 2

# Test the function with examples




def check(candidate):
    assert surfacearea_cube(5)==150
    assert surfacearea_cube(3)==54
    assert surfacearea_cube(10)==600

check(surfacearea_cube)