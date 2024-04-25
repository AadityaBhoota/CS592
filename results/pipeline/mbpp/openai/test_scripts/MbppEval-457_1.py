def Find_Min(lst):
    min_length = float('inf')
    min_sublist = None
    
    for sublist in lst:
        sublist_length = len(sublist)
        if sublist_length < min_length:
            min_length = sublist_length
            min_sublist = sublist
    
    return min_sublist

def check(candidate):
    assert Find_Min([[1],[1,2],[1,2,3]]) == [1]
    assert Find_Min([[1,1],[1,1,1],[1,2,7,8]]) == [1,1]
    assert Find_Min([['x'],['x','y'],['x','y','z']]) == ['x']

check(Find_Min)