def is_lower(string):
    """
    Write a python function to convert the given string to lower case.

    Examples:
    is_lower("InValid") == "invalid"
    is_lower("TruE") == "true"
    is_lower("SenTenCE") == "sentence"
    """
    return string.lower()

def check(candidate):
    assert is_lower("InValid") == "invalid"
    assert is_lower("TruE") == "true"
    assert is_lower("SenTenCE") == "sentence"

check(is_lower)