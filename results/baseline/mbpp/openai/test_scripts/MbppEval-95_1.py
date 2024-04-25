def Find_Min_Length(lst):  
    min_length = float('inf')  # Initialize with positive infinity
    
    for sub_list in lst:
        current_length = len(sub_list)
        if current_length < min_length:
            min_length = current_length
    
    return min_length

# Test cases




def check(candidate):
    assert Find_Min_Length([[1],[1,2]]) == 1
    assert Find_Min_Length([[1,2],[1,2,3],[1,2,3,4]]) == 2
    assert Find_Min_Length([[3,3,3],[4,4,4,4]]) == 3

check(Find_Min_Length)