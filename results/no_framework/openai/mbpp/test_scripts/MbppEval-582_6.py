def my_dict(dict1):
    return not bool(dict1)

# Test cases




def check(candidate):
    assert my_dict({10})==False
    assert my_dict({11})==False
    assert my_dict({})==True

check(my_dict)