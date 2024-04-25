import bisect

def left_insertion(a, x):
    left_index = bisect.bisect_left(a, x)
    return left_index

# Test the function




def check(candidate):
    assert left_insertion([1,2,4,5],6)==4
    assert left_insertion([1,2,4,5],3)==2
    assert left_insertion([1,2,4,5],7)==4

check(left_insertion)