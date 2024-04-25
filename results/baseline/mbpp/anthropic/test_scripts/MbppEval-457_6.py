def Find_Min(lst):
    """
    Write a python function to find the sublist having minimum length.

    Examples:
    Find_Min([[1],[1,2],[1,2,3]]) == [1]
    Find_Min([[1,1],[1,1,1],[1,2,7,8]]) == [1,1]
    Find_Min([['x'],['x','y'],['x','y','z']]) == ['x']
    """
    if not lst:
        return []

    min_length = min(len(sub) for sub in lst)
    return next(sub for sub in lst if len(sub) == min_length)

def check(candidate):
    assert Find_Min([[1],[1,2],[1,2,3]]) == [1]
    assert Find_Min([[1,1],[1,1,1],[1,2,7,8]]) == [1,1]
    assert Find_Min([['x'],['x','y'],['x','y','z']]) == ['x']

check(Find_Min)