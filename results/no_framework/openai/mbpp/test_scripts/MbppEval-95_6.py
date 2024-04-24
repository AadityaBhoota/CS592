def Find_Min_Length(lst):
    min_length = float('inf')  # Initialize min_length to positive infinity
    for sub_list in lst:
        # Update min_length if the length of the current sublist is smaller
        min_length = min(min_length, len(sub_list))
    return min_length

# Test the function with the provided examples




def check(candidate):
    assert Find_Min_Length([[1],[1,2]]) == 1
    assert Find_Min_Length([[1,2],[1,2,3],[1,2,3,4]]) == 2
    assert Find_Min_Length([[3,3,3],[4,4,4,4]]) == 3

check(Find_Min_Length)