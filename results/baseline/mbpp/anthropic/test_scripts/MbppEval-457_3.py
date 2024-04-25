def Find_Min(lst):
    """
    Find the sublist with the minimum length from a given list of lists.

    Args:
        lst (list): A list of lists.

    Returns:
        list: The sublist with the minimum length.
    """
    if not lst:
        return []

    min_length = float('inf')
    min_sublist = None

    for sublst in lst:
        if len(sublst) < min_length:
            min_length = len(sublst)
            min_sublist = sublst

    return min_sublist

def check(candidate):
    assert Find_Min([[1],[1,2],[1,2,3]]) == [1]
    assert Find_Min([[1,1],[1,1,1],[1,2,7,8]]) == [1,1]
    assert Find_Min([['x'],['x','y'],['x','y','z']]) == ['x']

check(Find_Min)