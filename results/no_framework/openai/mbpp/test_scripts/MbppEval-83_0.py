def get_Char(strr):
    total = sum(ord(ch) for ch in strr) % 26
    return chr(total + ord('a'))

# Test cases




def check(candidate):
    assert get_Char("abc") == "f"
    assert get_Char("gfg") == "t"
    assert get_Char("ab") == "c"

check(get_Char)