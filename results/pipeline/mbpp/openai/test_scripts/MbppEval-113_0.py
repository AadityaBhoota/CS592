def check_integer(text):
    if not isinstance(text, str):
        return False

    return text.isdigit()

def check(candidate):
    assert check_integer("python")==False
    assert check_integer("1")==True
    assert check_integer("12345")==True

check(check_integer)