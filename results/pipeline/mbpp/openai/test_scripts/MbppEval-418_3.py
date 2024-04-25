def Find_Max(lst): 
    max_length = 0
    slashed_str = None
    
    for element in lst:
        if len(element) > max_length:
            max_length = len(element)
            slashed_str = element 
    
    return slashed_str

def check(candidate):
    assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']
    assert Find_Max([[1],[1,2],[1,2,3]]) == [1,2,3]
    assert Find_Max([[1,1],[1,2,3],[1,5,6,1]]) == [1,5,6,1]

check(Find_Max)