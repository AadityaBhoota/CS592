def find_Average_Of_Cube(n):  
    total_cubes = 0
    for i in range(1, n + 1):
        cube = i ** 3
        total_cubes += cube
    avg_cube = total_cubes / n
    return avg_cube

def check(candidate):
    assert find_Average_Of_Cube(2) == 4.5
    assert find_Average_Of_Cube(3) == 12
    assert find_Average_Of_Cube(1) == 1

check(find_Average_Of_Cube)