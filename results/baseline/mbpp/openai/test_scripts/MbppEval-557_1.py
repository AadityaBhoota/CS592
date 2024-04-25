def toggle_string(string):
    return ''.join([char.lower() if char.isupper() else char.upper() for char in string])

# Test the function with the examples provided




def check(candidate):
    assert toggle_string("Python")==("pYTHON")
    assert toggle_string("Pangram")==("pANGRAM")
    assert toggle_string("LIttLE")==("liTTle")

check(toggle_string)