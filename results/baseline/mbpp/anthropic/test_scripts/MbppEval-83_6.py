def get_Char(strr):
    """
    Write a python function to find the character made by adding the ASCII value of all the characters of the given string modulo 26.

    Examples:
    get_Char("abc") == "f"
    get_Char("gfg") == "t"
    get_Char("ab") == "c"
    """
    total_ascii = 0
    for char in strr:
        total_ascii += ord(char)
    
    return chr((total_ascii % 26) + 65)

def check(candidate):
    assert get_Char("abc") == "f"
    assert get_Char("gfg") == "t"
    assert get_Char("ab") == "c"

check(get_Char)