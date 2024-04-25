def cube_Sum(n):
    total_sum = 0
    for i in range(1, n+1):
        even_number = 2 * i
        cube = even_number ** 3
        total_sum += cube
    return total_sum

def check(candidate):
    assert cube_Sum(2) == 72
    assert cube_Sum(3) == 288
    assert cube_Sum(4) == 800

check(cube_Sum)