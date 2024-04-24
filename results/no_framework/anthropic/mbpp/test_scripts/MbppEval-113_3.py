def check_integer(text):
    """
    Checks if a string represents an integer or not.

    Args:
        text (str): The string to be checked.

    Returns:
        bool: True if the string represents an integer, False otherwise.
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