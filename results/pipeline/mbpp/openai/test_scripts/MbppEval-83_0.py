def get_Char(strr):
    total_ascii = 0
    for char in strr:
        total_ascii += ord(char)
    total_ascii %= 26
    final_char = chr(total_ascii)
    return final_char

def check(candidate):
    assert get_Char("abc") == "f"
    assert get_Char("gfg") == "t"
    assert get_Char("ab") == "c"

check(get_Char)