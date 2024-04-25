def empty_dit(list1):
    '''
    Write a function to check whether all dictionaries in a list are empty or not.

    Examples:
    empty_dit([{},{},{}]) == True
    empty_dit([{1,2},{},{}]) == False
    empty_dit({}) == True
    '''
    if not isinstance(list1, list):
        return True
    
    return all(not dict_item for dict_item in list1)

def check(candidate):
    assert empty_dit([{},{},{}])==True
    assert empty_dit([{1,2},{},{}])==False
    assert empty_dit({})==True

check(empty_dit)