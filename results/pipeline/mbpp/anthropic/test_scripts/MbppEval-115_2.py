def empty_dit(list1):
    """
    Write a function to check whether all dictionaries in a list are empty or not.

    Examples:
    empty_dit([{},{},{}]) == True
    empty_dit([{1,2},{},{}]) == False
    empty_dit({}) == True
    """
    all_empty = True
    for item in list1:
        if isinstance(item, dict):
            if len(item) > 0:
                all_empty = False
                break
    return all_empty

def check(candidate):
    assert empty_dit([{},{},{}])==True
    assert empty_dit([{1,2},{},{}])==False
    assert empty_dit({})==True

check(empty_dit)