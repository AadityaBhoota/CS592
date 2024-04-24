def Find_Min_Length(lst):
    # Initialize min_length with a large number
    min_length = float('inf')
    
    # Iterate through the list of lists
    for l in lst:
        # If the length of the current list is less than the current min_length, update min_length
        if len(l) < min_length:
            min_length = len(l)
    
    return min_length

# Test cases




def check(candidate):
    assert Find_Min_Length([[1],[1,2]]) == 1
    assert Find_Min_Length([[1,2],[1,2,3],[1,2,3,4]]) == 2
    assert Find_Min_Length([[3,3,3],[4,4,4,4]]) == 3

check(Find_Min_Length)