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

    # Find the minimum length of the sublists
    min_length = min(len(sub) for sub in lst)

    # Find the sublists with the minimum length
    return [sub for sub in lst if len(sub) == min_length][0]

def check(candidate):
    assert Find_Min([[1],[1,2],[1,2,3]]) == [1]
    assert Find_Min([[1,1],[1,1,1],[1,2,7,8]]) == [1,1]
    assert Find_Min([['x'],['x','y'],['x','y','z']]) == ['x']

check(Find_Min)