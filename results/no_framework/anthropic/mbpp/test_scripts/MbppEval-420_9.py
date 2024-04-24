def cube_Sum(n):
    """
    Write a Python function to find the cube sum of the first n even natural numbers.

    Examples:
    cube_Sum(2) == 72
    cube_Sum(3) == 288
    cube_Sum(4) == 800
    """
    total = 0
    for i in range(1, n+1):
        total += (2*i)**3
    return total

def check(candidate):
    assert cube_Sum(2) == 72
    assert cube_Sum(3) == 288
    assert cube_Sum(4) == 800

check(cube_Sum)