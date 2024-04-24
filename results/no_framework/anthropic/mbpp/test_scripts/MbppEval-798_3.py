def _sum(arr):
    '''
    Write a python function to find the sum of an array.

    Examples:
    _sum([1, 2, 3]) == 6
    _sum([15, 12, 13, 10]) == 50
    _sum([0, 1, 2]) == 3
    '''
    return sum(arr)

def check(candidate):
    assert _sum([1, 2, 3]) == 6
    assert _sum([15, 12, 13, 10]) == 50
    assert _sum([0, 1, 2]) == 3

check(_sum)