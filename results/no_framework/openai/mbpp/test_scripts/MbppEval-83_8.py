def get_Char(strr):
    total = sum([ord(char) for char in strr])
    result = chr((total % 26) + 97)
    return result

# Test cases



def check(candidate):
    assert get_Char("abc") == "f"
    assert get_Char("gfg") == "t"
    assert get_Char("ab") == "c"

check(get_Char)