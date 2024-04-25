def jacobsthal_num(n):
    '''
    Calculates the nth Jacobsthal number.
    
    Parameters:
    n (int): The position of the Jacobsthal number to calculate.
    
    Returns:
    int: The nth Jacobsthal number.
    '''
    if n < 2:
        return n
    
    first = 0
    second = 1
    
    for _ in range(2, n):
        current = second + 2 * first
        first, second = second, current
    
    return second

def check(candidate):
    assert jacobsthal_num(5) == 11
    assert jacobsthal_num(2) == 1
    assert jacobsthal_num(4) == 5
    assert jacobsthal_num(13) == 2731

check(jacobsthal_num)