def replace_spaces(text):
    new_text = ""
    for char in text:
        if char.isspace():
            new_text += "_"
        elif char == "_":
            new_text += " "
        else:
            new_text += char
    return new_text

def check(candidate):
    assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
    assert replace_spaces('The_Avengers') == 'The Avengers'
    assert replace_spaces('Fast and Furious') == 'Fast_and_Furious'

check(replace_spaces)