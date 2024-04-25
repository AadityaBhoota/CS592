def is_lower(string):
    """
    Converts the given string to lowercase.

    Args:
        string (str): The input string to be converted to lowercase.

    Returns:
        str: The lowercase version of the input string.
    """
    return string.lower()

def check(candidate):
    assert is_lower("InValid") == "invalid"
    assert is_lower("TruE") == "true"
    assert is_lower("SenTenCE") == "sentence"

check(is_lower)