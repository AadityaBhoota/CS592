def cube_Sum(n): 
    result = 0
    for i in range(1, (2*n)+1, 2):
        result += (i**3)
    return result

# Test cases




def check(candidate):
    assert cube_Sum(2) == 72
    assert cube_Sum(3) == 288
    assert cube_Sum(4) == 800

check(cube_Sum)