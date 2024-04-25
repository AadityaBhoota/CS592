def cube_Sum(n):
    sum_cubes = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            sum_cubes += i**3
    return sum_cubes

def check(candidate):
    assert cube_Sum(2) == 72
    assert cube_Sum(3) == 288
    assert cube_Sum(4) == 800

check(cube_Sum)