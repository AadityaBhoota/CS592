def cube_Sum(n):
    if n <= 0:
        return 0
    else:
        return (n*(n+1))**2 * 2

# Test cases




def check(candidate):
    assert cube_Sum(2) == 72
    assert cube_Sum(3) == 288
    assert cube_Sum(4) == 800

check(cube_Sum)