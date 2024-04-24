def get_Char(strr):
    """
    Write a Python function to find the character made by adding the ASCII value of all the characters of the given string modulo 26.

    Examples:
    get_Char("abc") == "f"
    get_Char("gfg") == "t"
    get_Char("ab") == "c"
    """
    total_ascii = sum(ord(char) for char in strr)
    result_ascii = total_ascii % 26
    return chr(result_ascii + 97)

def check(candidate):
    assert get_Char("abc") == "f"
    assert get_Char("gfg") == "t"
    assert get_Char("ab") == "c"

check(get_Char)