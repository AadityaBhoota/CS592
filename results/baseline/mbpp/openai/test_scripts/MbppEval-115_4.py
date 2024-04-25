def empty_dit(list1):
    for dictionary in list1:
        if not isinstance(dictionary, dict):
            return False
        if dictionary:
            return False
    return True

# Test cases




def check(candidate):
    assert empty_dit([{},{},{}])==True
    assert empty_dit([{1,2},{},{}])==False
    assert empty_dit({})==True

check(empty_dit)