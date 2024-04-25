def Find_Max(lst):
    max_len = 0
    max_elem = []
    
    for elem in lst:
        if len(elem) > max_len:
            max_len = len(elem)
            max_elem = elem
    
    return max_elem

def check(candidate):
    assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']
    assert Find_Max([[1],[1,2],[1,2,3]]) == [1,2,3]
    assert Find_Max([[1,1],[1,2,3],[1,5,6,1]]) == [1,5,6,1]

check(Find_Max)