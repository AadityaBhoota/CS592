def get_Char(strr):
    total_sum = 0
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    for char in strr:
        total_sum += ord(char)
    
    index = total_sum % 26
    return alphabet[index]

def check(candidate):
    assert get_Char("abc") == "f"
    assert get_Char("gfg") == "t"
    assert get_Char("ab") == "c"

check(get_Char)