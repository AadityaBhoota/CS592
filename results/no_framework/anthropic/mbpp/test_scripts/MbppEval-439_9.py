def multiple_to_single(L):
    """
    Write a function to join a list of multiple integers into a single integer.

    Examples:
    multiple_to_single([11, 33, 50]) == 113350
    multiple_to_single([-1,2,3,4,5,6]) == -123456
    multiple_to_single([10,15,20,25]) == 10152025
    """
    result = 0
    sign = 1
    for num in L:
        if num < 0:
            sign = -1
        result = result * 10 + abs(num)
    return result * sign

def check(candidate):
    assert multiple_to_single([11, 33, 50])==113350
    assert multiple_to_single([-1,2,3,4,5,6])==-123456
    assert multiple_to_single([10,15,20,25])==10152025

check(multiple_to_single)