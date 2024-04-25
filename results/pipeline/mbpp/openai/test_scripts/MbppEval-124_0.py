import cmath

def angle_complex(a, b):
    return cmath.phase(a + b*1j)

def check(candidate):
    assert math.isclose(angle_complex(0,1j), 1.5707963267948966, rel_tol=0.001)
    assert math.isclose(angle_complex(2,1j), 0.4636476090008061, rel_tol=0.001)
    assert math.isclose(angle_complex(0,2j), 1.5707963267948966, rel_tol=0.001)

check(angle_complex)