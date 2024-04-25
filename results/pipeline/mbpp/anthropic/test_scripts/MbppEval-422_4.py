def find_Average_Of_Cube(n):
    total_cubes = 0
    for i in range(1, n+1):
        total_cubes += i**3
    return total_cubes / n

def check(candidate):
    assert find_Average_Of_Cube(2) == 4.5
    assert find_Average_Of_Cube(3) == 12
    assert find_Average_Of_Cube(1) == 1

check(find_Average_Of_Cube)