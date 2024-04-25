import bisect

def left_insertion(a, x):
    """
    Write a function to locate the left insertion point for a specified value in sorted order.
    
    Examples:
    left_insertion([1,2,4,5], 6) == 4
    left_insertion([1,2,4,5], 3) == 2
    left_insertion([1,2,4,5], 7) == 4
    """
    return bisect.bisect_left(a, x)

def check(candidate):
    assert left_insertion([1,2,4,5],6)==4
    assert left_insertion([1,2,4,5],3)==2
    assert left_insertion([1,2,4,5],7)==4

check(left_insertion)