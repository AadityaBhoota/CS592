def Find_Max(lst):
    max_length = 0
    max_element = None

    for sublst in lst:
        if len(sublst) > max_length:
            max_length = len(sublst)
            max_element = sublst

    return max_element

def check(candidate):
    assert Find_Max([['A'],['A','B'],['A','B','C']]) == ['A','B','C']
    assert Find_Max([[1],[1,2],[1,2,3]]) == [1,2,3]
    assert Find_Max([[1,1],[1,2,3],[1,5,6,1]]) == [1,5,6,1]

check(Find_Max)