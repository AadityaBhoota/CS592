def is_upper(string):
    """
    Write a python function to convert a given string to uppercase.

    Examples:
    is_upper("person") == "PERSON"
    is_upper("final") == "FINAL"
    is_upper("Valid") == "VALID"
    """
    return string.upper()

def check(candidate):
    assert is_upper("person") =="PERSON"
    assert is_upper("final") == "FINAL"
    assert is_upper("Valid") == "VALID"

check(is_upper)