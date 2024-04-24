def cube_Sum(n):
    sum = 0
    for i in range(1, n*2+1, 2):
        sum += i**3
    return sum

# Test cases




def check(candidate):
    assert cube_Sum(2) == 72
    assert cube_Sum(3) == 288
    assert cube_Sum(4) == 800

check(cube_Sum)