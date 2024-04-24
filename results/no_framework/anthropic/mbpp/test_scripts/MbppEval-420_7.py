def cube_Sum(n):
    """
    Write a python function to find the cube sum of first n even natural numbers.

    Examples:
    cube_Sum(2) == 72
    cube_Sum(3) == 288
    cube_Sum(4) == 800
    """
    return sum([(2 * i) ** 3 for i in range(1, n + 1)])

def check(candidate):
    assert cube_Sum(2) == 72
    assert cube_Sum(3) == 288
    assert cube_Sum(4) == 800

check(cube_Sum)