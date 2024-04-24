def check_str(string): 
    regex = '^[aeiouAEIOU][A-Za-z0-9_]*'
    if re.match(regex, string):
        return 'Valid'
    else:
        return 'Invalid'

# Testing the function




def check(candidate):
    assert check_str("annie")
    assert not check_str("dawood")
    assert check_str("Else")

check(check_str)