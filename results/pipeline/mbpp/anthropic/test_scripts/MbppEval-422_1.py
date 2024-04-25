def find_Average_Of_Cube(n):
    sum_of_numbers = n * (n + 1) / 2
    sum_of_cubes = n * (n + 1) * (2 * n + 1) / 6
    return sum_of_cubes / sum_of_numbers

def check(candidate):
    assert find_Average_Of_Cube(2) == 4.5
    assert find_Average_Of_Cube(3) == 12
    assert find_Average_Of_Cube(1) == 1

check(find_Average_Of_Cube)