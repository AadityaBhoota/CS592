def empty_dit(lst):
    """
    Write a function to check whether all dictionaries in a list are empty or not.

    Examples:
    empty_dit([{},{},{}]) == True
    empty_dit([{1,2},{},{}]) == False
    empty_dit({}) == True
    """
    if isinstance(lst, dict):
        return len(lst) == 0
    elif isinstance(lst, list):
        return all(len(d) == 0 for d in lst)
    else:
        raise TypeError("Input must be a list or a dictionary")

def check(candidate):
    assert empty_dit([{},{},{}])==True
    assert empty_dit([{1,2},{},{}])==False
    assert empty_dit({})==True

check(empty_dit)