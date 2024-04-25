def jacobsthal_num(n):
    """
    Write a function to find the nth Jacobsthal number.
    
    Examples:
    jacobsthal_num(5) == 11
    jacobsthal_num(2) == 1
    jacobsthal_num(4) == 5
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return jacobsthal_num(n-1) + 2 * jacobsthal_num(n-2)

def check(candidate):
    assert jacobsthal_num(5) == 11
    assert jacobsthal_num(2) == 1
    assert jacobsthal_num(4) == 5
    assert jacobsthal_num(13) == 2731

check(jacobsthal_num)