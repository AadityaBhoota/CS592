def jacobsthal_num(n):
    """
    Find the nth Jacobsthal number.

    The Jacobsthal sequence is a sequence of integers defined by the recurrence relation:
    J(n) = J(n-1) + 2 * J(n-2), with J(0) = 0 and J(1) = 1.

    Args:
        n (int): The index of the Jacobsthal number to be calculated.

    Returns:
        int: The nth Jacobsthal number.
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