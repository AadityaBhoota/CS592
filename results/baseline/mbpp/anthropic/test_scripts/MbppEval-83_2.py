def get_Char(strr):
    """
    Write a python function to find the character made by adding the ASCII value of all the characters of the given string modulo 26.

    Examples:
    get_Char("abc") == "f"
    get_Char("gfg") == "t"
    get_Char("ab") == "c"
    """
    # Convert the string to lowercase for simplicity
    strr = strr.lower()

    # Calculate the sum of ASCII values of all characters in the string
    ascii_sum = sum(ord(char) for char in strr)

    # Find the remainder when the ASCII sum is divided by 26
    remainder = ascii_sum % 26

    # Convert the remainder to the corresponding lowercase letter
    return chr(remainder + ord('a'))

def check(candidate):
    assert get_Char("abc") == "f"
    assert get_Char("gfg") == "t"
    assert get_Char("ab") == "c"

check(get_Char)