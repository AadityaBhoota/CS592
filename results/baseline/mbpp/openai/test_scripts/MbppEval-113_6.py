def check_integer(text):
    try:
        int(text)
        return True
    except ValueError:
        return False

# Testing the function




def check(candidate):
    assert check_integer("python")==False
    assert check_integer("1")==True
    assert check_integer("12345")==True

check(check_integer)