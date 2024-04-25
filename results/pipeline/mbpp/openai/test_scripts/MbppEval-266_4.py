def lateralsurface_cube(l):
    # Step 1: Define the function lateralsurface_cube with parameter l for side length
    lateral_surface_area = 4 * l * l  # Calculate lateral surface area of cube

    return lateral_surface_area

# Test the function with examples




def check(candidate):
    assert lateralsurface_cube(5)==100
    assert lateralsurface_cube(9)==324
    assert lateralsurface_cube(10)==400

check(lateralsurface_cube)