def get_Char(strr):
    total_ascii = 0
    for char in strr:
        total_ascii += ord(char)
        
    remainder = total_ascii % 26
    result_char = chr(remainder + 97)  # Adding 97 to get the ASCII corresponding to 'a'
    
    return result_char

def check(candidate):
    assert get_Char("abc") == "f"
    assert get_Char("gfg") == "t"
    assert get_Char("ab") == "c"

check(get_Char)