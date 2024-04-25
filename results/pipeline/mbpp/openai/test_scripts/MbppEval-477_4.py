def is_lower(string):
    # Step 1: Define the function is_lower that takes a string as input
    # Step 2: Use the lower method of strings to convert the given string to lowercase
    return string.lower()

def check(candidate):
    assert is_lower("InValid") == "invalid"
    assert is_lower("TruE") == "true"
    assert is_lower("SenTenCE") == "sentence"

check(is_lower)