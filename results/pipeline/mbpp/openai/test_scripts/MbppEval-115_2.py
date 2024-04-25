def empty_dit(list1):
    result = True
    
    for dictionary in list1:
        if dictionary:
            result = False
            break
    
    return result

def check(candidate):
    assert empty_dit([{},{},{}])==True
    assert empty_dit([{1,2},{},{}])==False
    assert empty_dit({})==True

check(empty_dit)