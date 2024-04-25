def Find_Min_Length(lst):  
    min_length = float('inf')
    for sub_lst in lst:
        if len(sub_lst) < min_length:
            min_length = len(sub_lst)
    return min_length

# Testing the function




def check(candidate):
    assert Find_Min_Length([[1],[1,2]]) == 1
    assert Find_Min_Length([[1,2],[1,2,3],[1,2,3,4]]) == 2
    assert Find_Min_Length([[3,3,3],[4,4,4,4]]) == 3

check(Find_Min_Length)