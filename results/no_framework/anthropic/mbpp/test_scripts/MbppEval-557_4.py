def toggle_string(string):
    """
    Write a function to toggle the case of all characters in a string.

    Examples:
    toggle_string("Python") == ("pYTHON")
    toggle_string("Pangram") == ("pANGRAM")
    toggle_string("LIttLE") == ("liTTle")
    """
    result = ""
    for char in string:
        if char.isupper():
            result += char.lower()
        else:
            result += char.upper()
    return result

def check(candidate):
    assert toggle_string("Python")==("pYTHON")
    assert toggle_string("Pangram")==("pANGRAM")
    assert toggle_string("LIttLE")==("liTTle")

check(toggle_string)