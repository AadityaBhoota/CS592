def toggle_string(string):
    """
    Write a function to toggle the case of all characters in a string.

    Examples:
    toggle_string("Python") == "pYTHON"
    toggle_string("Pangram") == "pANGRAM"
    toggle_string("LIttLE") == "liTTle"
    """
    return ''.join(c.lower() if c.isupper() else c.upper() for c in string)

def check(candidate):
    assert toggle_string("Python")==("pYTHON")
    assert toggle_string("Pangram")==("pANGRAM")
    assert toggle_string("LIttLE")==("liTTle")

check(toggle_string)