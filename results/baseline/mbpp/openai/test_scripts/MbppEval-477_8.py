def is_lower(string):
    return string.lower()

# Test cases




def check(candidate):
    assert is_lower("InValid") == "invalid"
    assert is_lower("TruE") == "true"
    assert is_lower("SenTenCE") == "sentence"

check(is_lower)