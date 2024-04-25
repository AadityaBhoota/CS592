def toggle_string(string):
    return ''.join([char.lower() if char.isupper() else char.upper() for char in string])

# Test cases




def check(candidate):
    assert toggle_string("Python")==("pYTHON")
    assert toggle_string("Pangram")==("pANGRAM")
    assert toggle_string("LIttLE")==("liTTle")

check(toggle_string)