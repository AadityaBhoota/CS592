def cube_Sum(n):
    if n <= 0:
        return 0

    total = 0
    for i in range(1, n+1):
        total += (2*i)**3

    return total

# Test cases




def check(candidate):
    assert cube_Sum(2) == 72
    assert cube_Sum(3) == 288
    assert cube_Sum(4) == 800

check(cube_Sum)