import bisect

def right_insertion(a, x):
    if not a:
        return 0
    return bisect.bisect_right(a, x)

def check(candidate):
    assert right_insertion([1,2,4,5],6)==4
    assert right_insertion([1,2,4,5],3)==2
    assert right_insertion([1,2,4,5],7)==4

check(right_insertion)