def Find_Min_Length(lst):
    """
    Write a python function to find the length of the smallest list in a list of lists.

    Examples:
    Find_Min_Length([[1],[1,2]]) == 1
    Find_Min_Length([[1,2],[1,2,3],[1,2,3,4]]) == 2
    Find_Min_Length([[3,3,3],[4,4,4,4]]) == 3
    """
    if not lst:
        return 0
    
    min_length = float('inf')
    for inner_list in lst:
        min_length = min(min_length, len(inner_list))
    
    return min_length

def check(candidate):
    assert Find_Min_Length([[1],[1,2]]) == 1
    assert Find_Min_Length([[1,2],[1,2,3],[1,2,3,4]]) == 2
    assert Find_Min_Length([[3,3,3],[4,4,4,4]]) == 3

check(Find_Min_Length)