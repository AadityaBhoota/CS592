def Find_Min(lst): 
    min_length = min(len(sublist) for sublist in lst)
    min_sublists = [sublist for sublist in lst if len(sublist) == min_length]
    return min_sublists

# Test cases




def check(candidate):
    assert Find_Min([[1],[1,2],[1,2,3]]) == [1]
    assert Find_Min([[1,1],[1,1,1],[1,2,7,8]]) == [1,1]
    assert Find_Min([['x'],['x','y'],['x','y','z']]) == ['x']

check(Find_Min)