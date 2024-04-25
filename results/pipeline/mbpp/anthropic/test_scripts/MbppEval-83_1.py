def get_Char(strr):
    """
    Write a python function to find the character made by adding the ASCII value of all the alphabetic characters of the given string modulo 26.

    Examples:
    get_Char("abc") == "f"
    get_Char("gfg") == "t"
    get_Char("ab") == "c"
    get_Char("a1b!c2") == "f"
    """
    total = 0
    for char in strr:
        if char.isalpha():
            total += ord(char.lower())
    return chr(total % 26 + 65)

def check(candidate):
    assert get_Char("abc") == "f"
    assert get_Char("gfg") == "t"
    assert get_Char("ab") == "c"

check(get_Char)