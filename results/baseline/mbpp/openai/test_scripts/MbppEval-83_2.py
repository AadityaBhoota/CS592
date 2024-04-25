def get_Char(strr):
    total = sum(ord(char) for char in strr) % 26
    return chr(ord('a') + total)

# Test cases




def check(candidate):
    assert get_Char("abc") == "f"
    assert get_Char("gfg") == "t"
    assert get_Char("ab") == "c"

check(get_Char)