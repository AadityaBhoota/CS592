def find_Average_Of_Cube(n):
    """
    Function to find the average of cubes of first n natural numbers.
    
    Args:
    n (int): Number of natural numbers to consider
    
    Returns:
    float: Average of cubes of first n natural numbers
    """

    if n < 1:
        return None

    sum_cubes = sum([i**3 for i in range(1, n+1)])
    average_cube = sum_cubes / n
    return average_cube

# Test cases




def check(candidate):
    assert find_Average_Of_Cube(2) == 4.5
    assert find_Average_Of_Cube(3) == 12
    assert find_Average_Of_Cube(1) == 1

check(find_Average_Of_Cube)