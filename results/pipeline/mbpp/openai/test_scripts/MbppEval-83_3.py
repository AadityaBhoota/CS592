def get_Char(strr):
    sum_ascii = 0
    for char in strr:
        ascii_val = ord(char)
        sum_ascii += ascii_val
    sum_mod_26 = sum_ascii % 26
    result_char = chr(sum_mod_26)
    return result_char

def check(candidate):
    assert get_Char("abc") == "f"
    assert get_Char("gfg") == "t"
    assert get_Char("ab") == "c"

check(get_Char)