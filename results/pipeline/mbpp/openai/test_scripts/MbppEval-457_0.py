def Find_Min(lst): 
    '''
    Write a python function to find the sublist having minimum length.

    Examples:
    Find_Min([[1],[1,2],[1,2,3]]) == [1]
    Find_Min([[1,1],[1,1,1],[1,2,7,8]]) == [1,1]
    Find_Min([['x'],['x','y'],['x','y','z']]) == ['x']
    '''
def find_min(lst): 
    min_length = float('inf')
    min_sublist = []
    
    for sublist in lst:
        if len(sublist) < min_length:
            min_length = len(sublist)
            min_sublist = sublist
    
    return min_sublist

def check(candidate):
    assert Find_Min([[1],[1,2],[1,2,3]]) == [1]
    assert Find_Min([[1,1],[1,1,1],[1,2,7,8]]) == [1,1]
    assert Find_Min([['x'],['x','y'],['x','y','z']]) == ['x']

check(Find_Min)