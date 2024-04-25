def my_dict(dict1):
    return len(dict1) == 0

def check(candidate):
    assert my_dict({10})==False
    assert my_dict({11})==False
    assert my_dict({})==True

check(my_dict)