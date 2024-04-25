def get_Char(strr):
    total = 0
    for char in strr:
        total += ord(char)
    return chr(total % 26 + 97)

def check(candidate):
    assert get_Char("abc") == "f"
    assert get_Char("gfg") == "t"
    assert get_Char("ab") == "c"

check(get_Char)