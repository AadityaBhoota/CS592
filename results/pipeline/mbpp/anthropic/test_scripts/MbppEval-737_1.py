import re

regex = '^[aeiouAEIOU][A-Za-z0-9_]*'

def check_str(string):
    if re.match(regex, string):
        return 'Valid'
    else:
        return 'Invalid'

def check(candidate):
    assert check_str("annie")
    assert not check_str("dawood")
    assert check_str("Else")

check(check_str)