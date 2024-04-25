def find_Average_Of_Cube(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer greater than zero."

    sum_cubes = sum(i**3 for i in range(1, n+1))
    average_cubes = sum_cubes / n
    return average_cubes

# Test cases




def check(candidate):
    assert find_Average_Of_Cube(2) == 4.5
    assert find_Average_Of_Cube(3) == 12
    assert find_Average_Of_Cube(1) == 1

check(find_Average_Of_Cube)