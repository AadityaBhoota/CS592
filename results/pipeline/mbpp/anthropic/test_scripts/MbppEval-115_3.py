def empty_dit(obj):
    """
    Write a function to check whether all dictionaries in a list are empty or not.

    Examples:
    empty_dit([{},{},{}]) == True
    empty_dit([{1,2},{},{}]) == False
    empty_dit({}) == True
    empty_dit([]) == True
    empty_dit([1, 2, 3]) == False
    """
    if isinstance(obj, dict):
        return len(obj) == 0
    elif isinstance(obj, list):
        if len(obj) == 0:
            return True
        for item in obj:
            if not isinstance(item, dict):
                return False
            if len(item) > 0:
                return False
        return True
    else:
        return False

def check(candidate):
    assert empty_dit([{},{},{}])==True
    assert empty_dit([{1,2},{},{}])==False
    assert empty_dit({})==True

check(empty_dit)