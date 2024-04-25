def find_min_diff(arr,n): 
    '''
    Write a python function to find the minimum difference between any two elements in a given array. 
    Examples:
    find_Min_Diff((1,5,3,19,18,25),6) == 1
    find_Min_Diff((4,3,2,6),4) == 1
    find_Min_Diff((30,5,20,9),4) == 4
    '''
if diff < min_diff:
    min_diff = diff
return min_diff

def check(candidate):
    assert find_min_diff((1,5,3,19,18,25),6) == 1
    assert find_min_diff((4,3,2,6),4) == 1
    assert find_min_diff((30,5,20,9),4) == 4

check(find_min_diff)