def lateralsurface_cube(l):
    # Step 4: As there are four lateral faces, the lateral surface area is 4 * l^2
    return 4 * l**2

def check(candidate):
    assert lateralsurface_cube(5)==100
    assert lateralsurface_cube(9)==324
    assert lateralsurface_cube(10)==400

check(lateralsurface_cube)