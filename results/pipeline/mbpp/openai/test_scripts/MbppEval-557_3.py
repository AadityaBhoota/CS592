def toggle_string(string):
    toggled_string = []
    for char in string:
        if char.isupper():
            toggled_string.append(char.lower())
        else:
            toggled_string.append(char.upper())
    
    return ''.join(toggled_string)

def check(candidate):
    assert toggle_string("Python")==("pYTHON")
    assert toggle_string("Pangram")==("pANGRAM")
    assert toggle_string("LIttLE")==("liTTle")

check(toggle_string)