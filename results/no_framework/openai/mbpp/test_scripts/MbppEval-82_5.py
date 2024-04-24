def volume_sphere(r):
    return (4/3) * math.pi * (r**3)

# Test the function with the provided examples




def check(candidate):
    assert math.isclose(volume_sphere(10), 4188.790204786391, rel_tol=0.001)
    assert math.isclose(volume_sphere(25), 65449.84694978735, rel_tol=0.001)
    assert math.isclose(volume_sphere(20), 33510.32163829113, rel_tol=0.001)

check(volume_sphere)