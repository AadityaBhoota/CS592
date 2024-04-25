def smallest_num(xs):
    '''
    Write a python function to find smallest number in a list.

    Examples:
    smallest_num([10, 20, 1, 45, 99]) == 1
    smallest_num([1, 2, 3]) == 1
    smallest_num([45, 46, 50, 60]) == 45
    '''
    if len(xs) == 0:
        return None
    return min(xs)

def check(candidate):
    assert smallest_num([10, 20, 1, 45, 99]) == 1
    assert smallest_num([1, 2, 3]) == 1
    assert smallest_num([45, 46, 50, 60]) == 45

check(smallest_num)