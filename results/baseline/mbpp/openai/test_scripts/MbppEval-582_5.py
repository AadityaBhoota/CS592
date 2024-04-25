def my_dict(dict1):
    if not dict1:
        return True
    else:
        return False

# Testing the function with the given examples




def check(candidate):
    assert my_dict({10})==False
    assert my_dict({11})==False
    assert my_dict({})==True

check(my_dict)