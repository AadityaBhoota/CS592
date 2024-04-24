def multiple_to_single(L):
    result = ''.join(map(str, L))
    return int(result)

# Test the function with the given examples




def check(candidate):
    assert multiple_to_single([11, 33, 50])==113350
    assert multiple_to_single([-1,2,3,4,5,6])==-123456
    assert multiple_to_single([10,15,20,25])==10152025

check(multiple_to_single)