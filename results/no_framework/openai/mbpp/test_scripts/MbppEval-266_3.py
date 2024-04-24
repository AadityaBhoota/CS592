def lateralsurface_cube(l):
    return 4 * l**2

# Testing the function with examples




def check(candidate):
    assert lateralsurface_cube(5)==100
    assert lateralsurface_cube(9)==324
    assert lateralsurface_cube(10)==400

check(lateralsurface_cube)