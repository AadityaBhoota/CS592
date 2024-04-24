def my_dict(dict1):
    '''
    Write a function to check if a dictionary is empty

    Examples:
    my_dict({10}) == False
    my_dict({11}) == False
    my_dict({}) == True
    '''
    if not dict1:
        return True
    else:
        return False

def check(candidate):
    assert my_dict({10})==False
    assert my_dict({11})==False
    assert my_dict({})==True

check(my_dict)