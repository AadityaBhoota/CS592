def check_integer(text):
    """
    Write a function to check if a string represents an integer or not.

    Examples:
    check_integer("python") == False
    check_integer("1") == True
    check_integer("12345") == True
    """
    try:
        int(text)
        return True
    except ValueError:
        return False

def check(candidate):
    assert check_integer("python")==False
    assert check_integer("1")==True
    assert check_integer("12345")==True

check(check_integer)