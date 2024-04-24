def Find_Max(lst):
    max_len = 0
    max_elem = []
    
    for item in lst:
        if len(item) > max_len:
            max_len = len(item)
            max_elem = item
    
    return max_elem

# Test cases




def check(candidate):
    assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']
    assert Find_Max([[1],[1,2],[1,2,3]]) == [1,2,3]
    assert Find_Max([[1,1],[1,2,3],[1,5,6,1]]) == [1,5,6,1]

check(Find_Max)