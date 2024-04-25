def my_dict(dict1):
    if len(dict1) == 0:
        return True
    else:
        return False

def check(candidate):
    assert my_dict({10})==False
    assert my_dict({11})==False
    assert my_dict({})==True

check(my_dict)