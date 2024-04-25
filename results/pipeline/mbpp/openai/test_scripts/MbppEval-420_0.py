def cube_Sum(n):
    even_numbers = [2*i for i in range(1, n+1)]
    cubes = [num**3 for num in even_numbers]
    cube_sum = sum(cubes)
    return cube_sum

def check(candidate):
    assert cube_Sum(2) == 72
    assert cube_Sum(3) == 288
    assert cube_Sum(4) == 800

check(cube_Sum)