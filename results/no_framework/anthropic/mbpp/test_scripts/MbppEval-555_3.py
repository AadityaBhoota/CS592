def difference(n):
    """
    Write a python function to find the difference between the sum of cubes of the first n natural numbers and the sum of the first n natural numbers.

    Examples:
    difference(3) == 30
    difference(5) == 210
    difference(2) == 6
    """
    sum_of_cubes = sum(i**3 for i in range(1, n+1))
    sum_of_numbers = sum(range(1, n+1))
    return sum_of_cubes - sum_of_numbers

def check(candidate):
    assert difference(3) == 30
    assert difference(5) == 210
    assert difference(2) == 6

check(difference)