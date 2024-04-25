def replace_spaces(text):
    replaced_text = ""
    for char in text:
        if char == ' ':
            replaced_text += '_'
        elif char == '_':
            replaced_text += ' '
        else:
            replaced_text += char
    return replaced_text

# Test cases




def check(candidate):
    assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'
    assert replace_spaces('The_Avengers') == 'The Avengers'
    assert replace_spaces('Fast and Furious') == 'Fast_and_Furious'

check(replace_spaces)