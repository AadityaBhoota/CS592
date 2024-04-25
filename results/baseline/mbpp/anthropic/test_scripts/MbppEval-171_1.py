import math

def perimeter_pentagon(a):
    '''
    Write a function to find the perimeter of a regular pentagon from the length of its sides.

    Examples:
    perimeter_pentagon(5) == 25
    perimeter_pentagon(10) == 50
    perimeter_pentagon(15) == 75
    '''
    return 5 * a

def check(candidate):
    assert perimeter_pentagon(5) == 25
    assert perimeter_pentagon(10) == 50
    assert perimeter_pentagon(15) == 75

check(perimeter_pentagon)