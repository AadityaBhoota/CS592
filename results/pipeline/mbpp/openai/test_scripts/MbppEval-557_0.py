def toggle_string(string):
    toggled_string = ""
    
    for char in string:
        toggled_char = char.lower() if char.isupper() else char.upper()
        toggled_string += toggled_char
        
    return toggled_string

def check(candidate):
    assert toggle_string("Python")==("pYTHON")
    assert toggle_string("Pangram")==("pANGRAM")
    assert toggle_string("LIttLE")==("liTTle")

check(toggle_string)