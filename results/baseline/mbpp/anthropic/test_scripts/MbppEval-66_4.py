def pos_count(lst):
    """
    Write a python function to count the number of positive numbers in a list.

    Examples:
    pos_count([1,-2,3,-4]) == 2
    pos_count([3,4,5,-1]) == 3
    pos_count([1,2,3,4]) == 4
    """
    return sum(1 for num in lst if num > 0)

def check(candidate):
    assert pos_count([1,-2,3,-4]) == 2
    assert pos_count([3,4,5,-1]) == 3
    assert pos_count([1,2,3,4]) == 4

check(pos_count)