def check_integer(text):
    if not text:
        return False

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