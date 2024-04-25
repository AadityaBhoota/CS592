def empty_dit(list1):
    '''
    Write a function to check whether all dictionaries in a list are empty or not.

    Examples:
    empty_dit([{},{},{}]) == True
    empty_dit([{1,2},{},{}]) == False
    empty_dit({}) == True
    '''
def empty_dict(list1):
    """
    Write a function to check whether all dictionaries in a list are empty or not.

    Examples:
    empty_dict([{},{},{}]) == True
    empty_dict([{1,2},{},{}]) == False
    empty_dict([{}]) == True
    """
    if isinstance(list1, dict):
        return len(list1) == 0
    elif isinstance(list1, list):
        return all(len(d) == 0 for d in list1)
    else:
        return False

def check(candidate):
    assert empty_dit([{},{},{}])==True
    assert empty_dit([{1,2},{},{}])==False
    assert empty_dit({})==True

check(empty_dit)