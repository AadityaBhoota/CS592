def Find_Min_Length(lst):
    min_length = float('inf')
    
    for l in lst:
        length = len(l)
        
        if length < min_length:
            min_length = length

    return min_length

def check(candidate):
    assert Find_Min_Length([[1],[1,2]]) == 1
    assert Find_Min_Length([[1,2],[1,2,3],[1,2,3,4]]) == 2
    assert Find_Min_Length([[3,3,3],[4,4,4,4]]) == 3

check(Find_Min_Length)