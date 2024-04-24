def difference(n):
    """
    Write a python function to find the difference between the sum of cubes of the first n natural numbers and the sum of the first n natural numbers.

    Examples:
    difference(3) == 30
    difference(5) == 210
    difference(2) == 6
    """
    # Calculate the sum of cubes of the first n natural numbers
    sum_of_cubes = sum(i**3 for i in range(1, n+1))
    
    # Calculate the sum of the first n natural numbers
    sum_of_numbers = sum(range(1, n+1))
    
    # Calculate the difference
    diff = sum_of_cubes - sum_of_numbers**2
    
    return diff

def check(candidate):
    assert difference(3) == 30
    assert difference(5) == 210
    assert difference(2) == 6

check(difference)