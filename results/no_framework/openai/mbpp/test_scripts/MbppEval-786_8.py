import bisect

def right_insertion(a, x):
    return bisect.bisect_right(a, x)

# Test cases




def check(candidate):
    assert right_insertion([1,2,4,5],6)==4
    assert right_insertion([1,2,4,5],3)==2
    assert right_insertion([1,2,4,5],7)==4

check(right_insertion)