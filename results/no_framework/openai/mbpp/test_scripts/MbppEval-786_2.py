import bisect

def right_insertion(a, x):
    insert_pos = bisect.bisect_right(a, x)
    return insert_pos

# Test cases




def check(candidate):
    assert right_insertion([1,2,4,5],6)==4
    assert right_insertion([1,2,4,5],3)==2
    assert right_insertion([1,2,4,5],7)==4

check(right_insertion)