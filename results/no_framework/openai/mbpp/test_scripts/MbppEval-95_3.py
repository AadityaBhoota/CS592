def Find_Min_Length(lst):
    min_length = float('inf')  # Initialize min_length to positive infinity
    
    for sublist in lst:
        min_length = min(min_length, len(sublist))  # Update min_length if the current sublist is smaller
    
    return min_length

# Test cases




def check(candidate):
    assert Find_Min_Length([[1],[1,2]]) == 1
    assert Find_Min_Length([[1,2],[1,2,3],[1,2,3,4]]) == 2
    assert Find_Min_Length([[3,3,3],[4,4,4,4]]) == 3

check(Find_Min_Length)