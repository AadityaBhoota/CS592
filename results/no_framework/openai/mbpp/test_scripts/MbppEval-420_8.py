def cube_Sum(n): 
    if n <= 0: 
        return 0
    
    sum_cube = sum([(2*i)**3 for i in range(1, n+1)])
    return sum_cube

# Test the function




def check(candidate):
    assert cube_Sum(2) == 72
    assert cube_Sum(3) == 288
    assert cube_Sum(4) == 800

check(cube_Sum)