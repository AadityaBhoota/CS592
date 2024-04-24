def min_of_three(a, b, c):
    """
    Write a function to find the minimum of three numbers.

    Examples:
    min_of_three(10, 20, 0) == 0
    min_of_three(19, 15, 18) == 15
    min_of_three(-10, -20, -30) == -30
    """
    return min(a, b, c)

def check(candidate):
    assert min_of_three(10,20,0)==0
    assert min_of_three(19,15,18)==15
    assert min_of_three(-10,-20,-30)==-30

check(min_of_three)