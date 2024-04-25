def multiple_to_single(L):
    single_int = int(''.join(str(i) for i in L))
    return single_int

# Test cases




def check(candidate):
    assert multiple_to_single([11, 33, 50])==113350
    assert multiple_to_single([-1,2,3,4,5,6])==-123456
    assert multiple_to_single([10,15,20,25])==10152025

check(multiple_to_single)