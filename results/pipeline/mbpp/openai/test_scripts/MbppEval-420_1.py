def cube_Sum(n):
    def cube(num):
        return num ** 3
    
    even_numbers = [2 * i for i in range(1, n+1)]
    cubes = [cube(num) for num in even_numbers]
    
    return sum(cubes)

def check(candidate):
    assert cube_Sum(2) == 72
    assert cube_Sum(3) == 288
    assert cube_Sum(4) == 800

check(cube_Sum)