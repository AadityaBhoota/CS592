def empty_dit(list1):
    """
    Write a function to check whether all dictionaries in a list are empty or not.

    Examples:
    empty_dit([{},{},{}]) == True
    empty_dit([{1,2},{},{}]) == False
    empty_dit({}) == True
    """
    if isinstance(list1, dict):
        return len(list1) == 0
    elif isinstance(list1, list):
        for item in list1:
            if not isinstance(item, dict) or len(item) > 0:
                return False
        return True
    else:
        return False

def check(candidate):
    assert empty_dit([{},{},{}])==True
    assert empty_dit([{1,2},{},{}])==False
    assert empty_dit({})==True

check(empty_dit)