def frequency(a, x): 
    return a.count(x)

# Testing the function with provided examples
assert frequency([1,2,3], 4) == 0
assert frequency([1,2,2,3,3,3,4], 3) == 3
assert frequency([0,1,2,3,1,2], 1) == 2

def check(candidate):
    assert frequency([1,2,3], 4) == 0
    assert frequency([1,2,2,3,3,3,4], 3) == 3
    assert frequency([0,1,2,3,1,2], 1) == 2

check(frequency)