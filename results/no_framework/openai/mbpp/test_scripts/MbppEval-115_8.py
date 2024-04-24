def empty_dit(list1):
    for dictionary in list1:
        if dictionary:  # Check if the dictionary is not empty
            return False
    return True

# Test the function with examples




def check(candidate):
    assert empty_dit([{},{},{}])==True
    assert empty_dit([{1,2},{},{}])==False
    assert empty_dit({})==True

check(empty_dit)