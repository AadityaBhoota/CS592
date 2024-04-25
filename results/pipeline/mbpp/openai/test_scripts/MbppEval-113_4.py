def check_integer(text):
    if not text:
        return False

    for char in text:
        if not char.isdigit():
            return False

    return True

def check(candidate):
    assert check_integer("python")==False
    assert check_integer("1")==True
    assert check_integer("12345")==True

check(check_integer)