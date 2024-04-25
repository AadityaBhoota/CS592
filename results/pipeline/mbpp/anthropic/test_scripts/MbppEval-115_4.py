def empty_dit(list1):
    all_empty = True
    for element in list1:
        if isinstance(element, dict):
            if element:
                all_empty = False
                break
    return all_empty

def check(candidate):
    assert empty_dit([{},{},{}])==True
    assert empty_dit([{1,2},{},{}])==False
    assert empty_dit({})==True

check(empty_dit)