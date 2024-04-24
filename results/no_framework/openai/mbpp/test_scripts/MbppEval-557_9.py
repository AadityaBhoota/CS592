def toggle_string(string):
    toggled_string = ""
    for char in string:
        if char.islower():
            toggled_string += char.upper()
        else:
            toggled_string += char.lower()
    return toggled_string

# Test cases




def check(candidate):
    assert toggle_string("Python")==("pYTHON")
    assert toggle_string("Pangram")==("pANGRAM")
    assert toggle_string("LIttLE")==("liTTle")

check(toggle_string)