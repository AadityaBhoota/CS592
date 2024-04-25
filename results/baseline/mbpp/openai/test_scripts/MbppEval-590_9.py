import cmath

def polar_rect(r, theta):
    # Convert polar coordinates to rectangular coordinates using the formula z = r * (cos(theta) + i*sin(theta))
    rect = cmath.rect(r, cmath.pi * theta / 180)
    return (abs(rect), cmath.phase(rect)), rect

# Test cases




def check(candidate):
    assert polar_rect(3,4)==((5.0, 0.9272952180016122), (-2+2.4492935982947064e-16j))
    assert polar_rect(4,7)==((8.06225774829855, 1.0516502125483738), (-2+2.4492935982947064e-16j))
    assert polar_rect(15,17)==((22.67156809750927, 0.8478169733934057), (-2+2.4492935982947064e-16j))

check(polar_rect)