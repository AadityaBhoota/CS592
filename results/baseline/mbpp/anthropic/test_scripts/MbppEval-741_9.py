def all_Characters_Same(s):
    """
    Write a python function to check whether all the characters are same or not.

    Examples:
    all_Characters_Same("python") == False
    all_Characters_Same("aaa") == True
    all_Characters_Same("data") == False
    """
    if len(set(s)) == 1:
        return True
    else:
        return False

def check(candidate):
    assert all_Characters_Same("python") == False
    assert all_Characters_Same("aaa") == True
    assert all_Characters_Same("data") == False

check(all_Characters_Same)