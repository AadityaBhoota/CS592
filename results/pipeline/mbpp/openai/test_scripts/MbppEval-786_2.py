import bisect

def right_insertion(a, x):
    if not a:
        return 0
    
    if x > a[-1]:
        return len(a)
    
    insertion_point = bisect.bisect_right(a, x)
    
    return insertion_point

def check(candidate):
    assert right_insertion([1,2,4,5],6)==4
    assert right_insertion([1,2,4,5],3)==2
    assert right_insertion([1,2,4,5],7)==4

check(right_insertion)