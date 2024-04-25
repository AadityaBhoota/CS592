def smallest_num(xs):
    '''
    Find the smallest number in a list.
    
    Parameters:
    xs (list): A list of numbers
    
    Returns:
    int: The smallest number in the list
    '''
    if not xs:
        return None
    
    smallest = xs[0]
    
    for num in xs:
        if num < smallest:
            smallest = num
            
    return smallest

def check(candidate):
    assert smallest_num([10, 20, 1, 45, 99]) == 1
    assert smallest_num([1, 2, 3]) == 1
    assert smallest_num([45, 46, 50, 60]) == 45

check(smallest_num)