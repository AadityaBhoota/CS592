def is_upper(string):
    return string.upper()

# Test cases




def check(candidate):
    assert is_upper("person") =="PERSON"
    assert is_upper("final") == "FINAL"
    assert is_upper("Valid") == "VALID"

check(is_upper)