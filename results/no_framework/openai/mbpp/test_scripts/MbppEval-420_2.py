def cube_Sum(n):
    # Calculate the sum of cubes of first n even natural numbers
    cube_sum = sum([(2*i)**3 for i in range(1, n+1)])

    return cube_sum

# Test cases




def check(candidate):
    assert cube_Sum(2) == 72
    assert cube_Sum(3) == 288
    assert cube_Sum(4) == 800

check(cube_Sum)